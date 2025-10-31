#!/usr/bin/env python3
"""
Automated Lead Finder - Find businesses with poor Google Business Profiles

This tool searches for businesses in your target area and identifies those
with incomplete or poor profiles (low photo counts, few reviews, etc.)

Usage:
    python lead_finder.py "Seattle, WA" --industry "coffee shop"
    python lead_finder.py "Austin, TX" --industry "salon" --limit 50
    python lead_finder.py "Denver, CO" --demo  # Demo mode without API
"""

import os
import sys
import json
import argparse
import csv
from datetime import datetime
from typing import List, Dict, Optional
import requests
import time


class LeadFinder:
    """Find and qualify leads for GBP optimization services"""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize lead finder with optional Google API key"""
        self.api_key = api_key or os.getenv('GOOGLE_PLACES_API_KEY')
        self.base_url = "https://maps.googleapis.com/maps/api/place"

    def search_businesses(self, query: str, location: str, limit: int = 20) -> List[Dict]:
        """Search for businesses matching query in location"""

        if not self.api_key:
            print("⚠️  No API key found. Using demo mode.")
            return self._generate_demo_leads(query, location, limit)

        print(f"\n🔍 Searching for '{query}' in {location}...")

        search_url = f"{self.base_url}/textsearch/json"
        params = {
            'query': f"{query} in {location}",
            'key': self.api_key
        }

        try:
            response = requests.get(search_url, params=params)
            response.raise_for_status()
            results = response.json().get('results', [])

            print(f"✓ Found {len(results)} businesses")
            return results[:limit]

        except Exception as e:
            print(f"❌ API Error: {e}")
            print("⚠️  Falling back to demo mode...")
            return self._generate_demo_leads(query, location, limit)

    def get_business_details(self, place_id: str) -> Dict:
        """Get detailed information for a business"""

        details_url = f"{self.base_url}/details/json"
        params = {
            'place_id': place_id,
            'fields': 'name,rating,user_ratings_total,photos,opening_hours,formatted_phone_number,website,formatted_address,types',
            'key': self.api_key
        }

        try:
            response = requests.get(details_url, params=params)
            response.raise_for_status()
            return response.json().get('result', {})
        except Exception as e:
            print(f"  ⚠️ Could not fetch details: {e}")
            return {}

    def score_lead_quality(self, business: Dict) -> Dict:
        """Score lead quality (higher score = better opportunity)"""

        score = 0
        reasons = []

        # Get details
        photo_count = len(business.get('photos', []))
        review_count = business.get('user_ratings_total', 0)
        has_phone = bool(business.get('formatted_phone_number'))
        has_website = bool(business.get('website'))
        has_hours = bool(business.get('opening_hours'))

        # Scoring logic (higher score = better lead)
        if photo_count < 10:
            score += 30
            reasons.append(f"Only {photo_count} photos (needs 20+)")

        if review_count < 30:
            score += 20
            reasons.append(f"Only {review_count} reviews (low social proof)")

        if not has_website:
            score += 15
            reasons.append("No website listed")

        if not has_hours:
            score += 15
            reasons.append("Missing business hours")

        # Established but needs help (sweet spot)
        if 5 <= review_count <= 50:
            score += 20
            reasons.append("Established business (has reviews)")

        # Rating indicates they care about reputation
        rating = business.get('rating', 0)
        if rating >= 4.0:
            score += 10
            reasons.append("Good rating (cares about reputation)")

        return {
            'score': score,
            'priority': 'HIGH' if score >= 60 else 'MEDIUM' if score >= 40 else 'LOW',
            'reasons': reasons,
            'photo_count': photo_count,
            'review_count': review_count,
            'rating': rating,
            'has_phone': has_phone,
            'has_website': has_website,
            'has_hours': has_hours
        }

    def find_leads(self, query: str, location: str, limit: int = 20,
                   min_score: int = 40) -> List[Dict]:
        """Find and qualify leads"""

        # Search for businesses
        businesses = self.search_businesses(query, location, limit)

        leads = []

        print(f"\n📊 Analyzing {len(businesses)} businesses...\n")

        for i, biz in enumerate(businesses, 1):
            # Get details if we have API
            if self.api_key and 'place_id' in biz:
                time.sleep(0.5)  # Rate limiting
                details = self.get_business_details(biz['place_id'])
                biz.update(details)

            # Score the lead
            score_data = self.score_lead_quality(biz)

            if score_data['score'] >= min_score:
                lead = {
                    'business_name': biz.get('name', 'Unknown'),
                    'address': biz.get('formatted_address', ''),
                    'phone': biz.get('formatted_phone_number', ''),
                    'website': biz.get('website', ''),
                    'rating': score_data['rating'],
                    'reviews': score_data['review_count'],
                    'photos': score_data['photo_count'],
                    'score': score_data['score'],
                    'priority': score_data['priority'],
                    'reasons': '; '.join(score_data['reasons'][:2]),  # Top 2 reasons
                    'place_id': biz.get('place_id', '')
                }

                leads.append(lead)

                # Print progress
                status = '🔥' if lead['priority'] == 'HIGH' else '⚡' if lead['priority'] == 'MEDIUM' else '💡'
                print(f"{status} {lead['business_name']}")
                print(f"   Score: {lead['score']} | Priority: {lead['priority']}")
                print(f"   {lead['reasons']}")
                print()

        # Sort by score (highest first)
        leads.sort(key=lambda x: x['score'], reverse=True)

        return leads

    def save_leads(self, leads: List[Dict], output_file: str = None):
        """Save leads to CSV file"""

        if not leads:
            print("❌ No leads to save")
            return

        if not output_file:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            output_file = f"leads/leads_{timestamp}.csv"

        os.makedirs(os.path.dirname(output_file), exist_ok=True)

        fieldnames = ['priority', 'score', 'business_name', 'phone', 'address',
                     'rating', 'reviews', 'photos', 'website', 'reasons', 'place_id']

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(leads)

        print(f"\n✅ Saved {len(leads)} leads to: {output_file}")

    def _generate_demo_leads(self, query: str, location: str, limit: int) -> List[Dict]:
        """Generate demo leads for testing without API"""
        import random

        print(f"🎭 Generating {limit} demo leads...")

        # Extract business type from query
        business_type = query.lower()

        demo_leads = []

        for i in range(limit):
            # Generate realistic business name
            if 'coffee' in business_type or 'cafe' in business_type:
                names = ["Joe's Coffee", "Brew Haven", "Morning Grind", "Bean There", "Espresso Express"]
                suffixes = ["Cafe", "Coffee House", "Roasters", "Bar", "Shop"]
            elif 'salon' in business_type or 'barber' in business_type:
                names = ["Bella's Hair", "Style Studio", "The Cut", "Perfect Look", "Glamour"]
                suffixes = ["Salon", "Studio", "Barber Shop", "Spa", "Lounge"]
            elif 'gym' in business_type or 'fitness' in business_type:
                names = ["Peak Performance", "Iron Works", "Fit Zone", "Power", "CrossFit"]
                suffixes = ["Gym", "Fitness", "Training Center", "Studio", "Box"]
            elif 'plumb' in business_type or 'hvac' in business_type:
                names = ["Quick Fix", "Pro", "24/7", "Reliable", "Expert"]
                suffixes = ["Plumbing", "HVAC", "Services", "Repairs", "Solutions"]
            else:
                names = ["Local", "City", "Best", "Premier", "Quality"]
                suffixes = ["Services", "Company", "Shop", "Store", "Business"]

            business_name = f"{random.choice(names)} {random.choice(suffixes)}"

            # Extract city from location
            city = location.split(',')[0].strip()

            demo_leads.append({
                'name': business_name,
                'formatted_address': f"{random.randint(100, 9999)} Main St, {location}",
                'formatted_phone_number': f"(555) {random.randint(100, 999)}-{random.randint(1000, 9999)}",
                'website': '' if random.random() > 0.4 else f"https://www.{business_name.lower().replace(' ', '')}.com",
                'rating': round(random.uniform(3.5, 4.8), 1),
                'user_ratings_total': random.randint(5, 45),
                'photos': [{'ref': f'photo_{i}'} for i in range(random.randint(2, 8))],
                'opening_hours': {'open_now': True} if random.random() > 0.2 else None,
                'place_id': f'demo_place_{i}'
            })

        return demo_leads


def main():
    """Main CLI entry point"""

    parser = argparse.ArgumentParser(
        description='Find high-quality leads for GBP optimization services'
    )
    parser.add_argument('location', nargs='?', default='Seattle, WA',
                       help='City, State to search (e.g., "Austin, TX")')
    parser.add_argument('--industry', default='coffee shop',
                       help='Industry to target (e.g., "salon", "gym", "plumber")')
    parser.add_argument('--limit', type=int, default=20,
                       help='Number of businesses to search (default: 20)')
    parser.add_argument('--min-score', type=int, default=40,
                       help='Minimum lead quality score (default: 40)')
    parser.add_argument('--output', help='Output CSV file path')
    parser.add_argument('--demo', action='store_true',
                       help='Use demo mode (no API required)')
    parser.add_argument('--api-key', help='Google Places API key')

    args = parser.parse_args()

    # Initialize finder
    api_key = None if args.demo else args.api_key
    finder = LeadFinder(api_key=api_key)

    # Find leads
    leads = finder.find_leads(
        query=args.industry,
        location=args.location,
        limit=args.limit,
        min_score=args.min_score
    )

    # Summary
    if leads:
        high_priority = sum(1 for lead in leads if lead['priority'] == 'HIGH')
        medium_priority = sum(1 for lead in leads if lead['priority'] == 'MEDIUM')

        print("=" * 60)
        print(f"📊 LEAD SUMMARY")
        print("=" * 60)
        print(f"Total Qualified Leads: {len(leads)}")
        print(f"🔥 High Priority: {high_priority}")
        print(f"⚡ Medium Priority: {medium_priority}")
        print()
        print("Top 3 Leads:")
        for i, lead in enumerate(leads[:3], 1):
            print(f"{i}. {lead['business_name']} (Score: {lead['score']})")
            print(f"   {lead['reasons']}")
        print()

        # Save to file
        finder.save_leads(leads, args.output)

        print("\n💡 NEXT STEPS:")
        print("1. Review the leads CSV file")
        print("2. Generate audit reports for top leads:")
        print(f"   python tools/gbp_audit.py \"[Business Name]\" \"{args.location}\"")
        print("3. Send personalized emails with audit reports")
        print("4. Follow up by phone or walk-in")
    else:
        print("❌ No qualified leads found. Try:")
        print("  - Lower --min-score threshold")
        print("  - Different industry")
        print("  - Different location")


if __name__ == '__main__':
    main()
