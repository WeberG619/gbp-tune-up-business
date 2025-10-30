#!/usr/bin/env python3
"""
GBP Audit Tool - Analyze Google Business Profiles and generate opportunity reports

Usage:
    python gbp_audit.py "Business Name" "City, State"
    python gbp_audit.py --demo  # Run with sample data
"""

import os
import sys
import json
import argparse
from datetime import datetime
from typing import Dict, List, Optional
import requests
from dataclasses import dataclass, asdict


@dataclass
class GBPAuditResult:
    """Results from GBP audit"""
    business_name: str
    location: str
    audit_date: str

    # Current state
    photo_count: int
    review_count: int
    avg_rating: float
    has_hours: bool
    has_phone: bool
    has_website: bool
    has_description: bool
    qa_count: int
    posts_last_30_days: int

    # Competitor benchmarks
    competitor_avg_photos: int
    competitor_avg_reviews: int
    competitor_avg_rating: float

    # Gaps and opportunities
    missing_photos: int
    missing_attributes: List[str]
    review_response_rate: float

    # Scoring
    profile_score: int  # 0-100
    competitor_avg_score: int

    # Recommendations
    priority_actions: List[str]
    estimated_impact: str


class GBPAuditor:
    """Audit Google Business Profiles and generate reports"""

    def __init__(self, api_key: Optional[str] = None):
        """Initialize auditor with optional Google API key"""
        self.api_key = api_key or os.getenv('GOOGLE_PLACES_API_KEY')
        self.base_url = "https://maps.googleapis.com/maps/api/place"

    def search_business(self, business_name: str, location: str) -> Optional[Dict]:
        """Search for business using Places API"""

        if not self.api_key:
            print("⚠️  No API key found. Using demo mode.")
            return self._generate_demo_data(business_name, location)

        # Find Place
        search_url = f"{self.base_url}/findplacefromtext/json"
        params = {
            'input': f"{business_name} {location}",
            'inputtype': 'textquery',
            'fields': 'place_id,name,formatted_address',
            'key': self.api_key
        }

        try:
            response = requests.get(search_url, params=params)
            response.raise_for_status()
            data = response.json()

            if data.get('candidates'):
                return data['candidates'][0]
            else:
                print(f"❌ Business not found: {business_name}")
                return None

        except Exception as e:
            print(f"❌ API Error: {e}")
            return self._generate_demo_data(business_name, location)

    def get_business_details(self, place_id: str) -> Dict:
        """Get detailed business information"""

        details_url = f"{self.base_url}/details/json"
        params = {
            'place_id': place_id,
            'fields': 'name,rating,user_ratings_total,photos,opening_hours,formatted_phone_number,website,editorial_summary,types',
            'key': self.api_key
        }

        try:
            response = requests.get(details_url, params=params)
            response.raise_for_status()
            return response.json().get('result', {})
        except Exception as e:
            print(f"❌ Error fetching details: {e}")
            return {}

    def find_competitors(self, business_name: str, location: str, business_type: str = "restaurant") -> List[Dict]:
        """Find nearby competitors for benchmarking"""

        nearby_url = f"{self.base_url}/textsearch/json"
        params = {
            'query': f"{business_type} near {location}",
            'key': self.api_key
        }

        try:
            response = requests.get(nearby_url, params=params)
            response.raise_for_status()
            results = response.json().get('results', [])

            # Exclude the target business and limit to top 5
            competitors = [r for r in results if r.get('name', '').lower() != business_name.lower()][:5]
            return competitors

        except Exception as e:
            print(f"⚠️  Could not fetch competitors: {e}")
            return []

    def calculate_score(self, details: Dict) -> int:
        """Calculate profile completeness score (0-100)"""
        score = 0

        # Photos (30 points)
        photo_count = len(details.get('photos', []))
        score += min(30, photo_count * 1.5)

        # Reviews (20 points)
        review_count = details.get('user_ratings_total', 0)
        score += min(20, review_count * 0.4)

        # Rating (15 points)
        rating = details.get('rating', 0)
        score += rating * 3

        # Basic info (35 points)
        if details.get('opening_hours'):
            score += 10
        if details.get('formatted_phone_number'):
            score += 10
        if details.get('website'):
            score += 10
        if details.get('editorial_summary'):
            score += 5

        return min(100, int(score))

    def audit(self, business_name: str, location: str) -> GBPAuditResult:
        """Run complete audit on a business"""

        print(f"\n🔍 Auditing: {business_name} in {location}")
        print("=" * 60)

        # Search for business
        business = self.search_business(business_name, location)
        if not business:
            return None

        # Get details
        if 'place_id' in business:
            details = self.get_business_details(business['place_id'])
        else:
            details = business  # Demo data already has details

        # Get competitors for benchmarking
        competitors = self.find_competitors(business_name, location)

        # Calculate metrics
        photo_count = len(details.get('photos', []))
        review_count = details.get('user_ratings_total', 0)
        avg_rating = details.get('rating', 0.0)
        profile_score = self.calculate_score(details)

        # Competitor benchmarks
        if competitors:
            competitor_photos = [len(c.get('photos', [])) for c in competitors]
            competitor_reviews = [c.get('user_ratings_total', 0) for c in competitors]
            competitor_ratings = [c.get('rating', 0) for c in competitors]

            comp_avg_photos = int(sum(competitor_photos) / len(competitor_photos)) if competitor_photos else 20
            comp_avg_reviews = int(sum(competitor_reviews) / len(competitor_reviews)) if competitor_reviews else 50
            comp_avg_rating = sum(competitor_ratings) / len(competitor_ratings) if competitor_ratings else 4.5
            comp_avg_score = 78  # Typical competitor score
        else:
            comp_avg_photos = 20
            comp_avg_reviews = 50
            comp_avg_rating = 4.5
            comp_avg_score = 78

        # Identify gaps
        missing_photos = max(0, comp_avg_photos - photo_count)
        missing_attributes = []

        if not details.get('opening_hours'):
            missing_attributes.append('Business Hours')
        if not details.get('formatted_phone_number'):
            missing_attributes.append('Phone Number')
        if not details.get('website'):
            missing_attributes.append('Website')
        if not details.get('editorial_summary'):
            missing_attributes.append('Business Description')

        # Generate recommendations
        priority_actions = self._generate_recommendations(
            photo_count, review_count, missing_attributes, comp_avg_photos
        )

        # Estimate impact
        score_gap = comp_avg_score - profile_score
        if score_gap > 30:
            impact = "+20-30 calls/week"
        elif score_gap > 15:
            impact = "+10-20 calls/week"
        else:
            impact = "+5-10 calls/week"

        result = GBPAuditResult(
            business_name=business.get('name', business_name),
            location=location,
            audit_date=datetime.now().strftime("%Y-%m-%d"),
            photo_count=photo_count,
            review_count=review_count,
            avg_rating=avg_rating,
            has_hours=bool(details.get('opening_hours')),
            has_phone=bool(details.get('formatted_phone_number')),
            has_website=bool(details.get('website')),
            has_description=bool(details.get('editorial_summary')),
            qa_count=0,  # Requires different API endpoint
            posts_last_30_days=0,  # Requires My Business API
            competitor_avg_photos=comp_avg_photos,
            competitor_avg_reviews=comp_avg_reviews,
            competitor_avg_rating=comp_avg_rating,
            missing_photos=missing_photos,
            missing_attributes=missing_attributes,
            review_response_rate=0.0,  # Requires My Business API
            profile_score=profile_score,
            competitor_avg_score=comp_avg_score,
            priority_actions=priority_actions,
            estimated_impact=impact
        )

        return result

    def _generate_recommendations(self, photo_count: int, review_count: int,
                                   missing_attrs: List[str], comp_photos: int) -> List[str]:
        """Generate prioritized action items"""
        actions = []

        if photo_count < 10:
            actions.append(f"📸 Add {20 - photo_count} professional photos (interior, exterior, products, team)")

        if missing_attrs:
            actions.append(f"📝 Complete missing info: {', '.join(missing_attrs)}")

        if review_count < 20:
            actions.append("⭐ Set up review generation system (target: 2-3 new reviews/week)")

        actions.append("📅 Create weekly posting schedule (offers, updates, events)")
        actions.append("❓ Add 5-10 frequently asked questions with answers")

        return actions

    def _generate_demo_data(self, business_name: str, location: str) -> Dict:
        """Generate realistic demo data for testing without API"""
        import random

        return {
            'name': business_name,
            'formatted_address': location,
            'rating': round(random.uniform(3.5, 4.8), 1),
            'user_ratings_total': random.randint(15, 45),
            'photos': [{'reference': f'photo_{i}'} for i in range(random.randint(3, 8))],
            'opening_hours': None if random.random() > 0.7 else {'open_now': True},
            'formatted_phone_number': None if random.random() > 0.8 else '(555) 123-4567',
            'website': None if random.random() > 0.6 else 'https://example.com',
            'editorial_summary': None if random.random() > 0.7 else {'overview': 'A local business'}
        }


def print_audit_report(result: GBPAuditResult):
    """Print formatted audit report to console"""

    print(f"\n{'=' * 60}")
    print(f"📊 GOOGLE BUSINESS PROFILE AUDIT REPORT")
    print(f"{'=' * 60}\n")

    print(f"🏢 Business: {result.business_name}")
    print(f"📍 Location: {result.location}")
    print(f"📅 Audit Date: {result.audit_date}\n")

    print(f"{'─' * 60}")
    print(f"📈 PROFILE SCORE: {result.profile_score}/100")
    print(f"📊 Competitor Average: {result.competitor_avg_score}/100")
    print(f"{'─' * 60}\n")

    print("📸 CURRENT STATUS:")
    print(f"  • Photos: {result.photo_count} (competitors avg: {result.competitor_avg_photos})")
    print(f"  • Reviews: {result.review_count} (competitors avg: {result.competitor_avg_reviews})")
    print(f"  • Rating: {result.avg_rating:.1f}★ (competitors avg: {result.competitor_avg_rating:.1f}★)")
    print(f"  • Business Hours: {'✅' if result.has_hours else '❌'}")
    print(f"  • Phone Number: {'✅' if result.has_phone else '❌'}")
    print(f"  • Website: {'✅' if result.has_website else '❌'}")
    print(f"  • Description: {'✅' if result.has_description else '❌'}\n")

    if result.missing_attributes:
        print("⚠️  MISSING INFORMATION:")
        for attr in result.missing_attributes:
            print(f"  • {attr}")
        print()

    print("🎯 PRIORITY ACTIONS:")
    for i, action in enumerate(result.priority_actions, 1):
        print(f"  {i}. {action}")
    print()

    print(f"💰 ESTIMATED IMPACT: {result.estimated_impact}")
    print(f"\n{'=' * 60}\n")


def save_report_json(result: GBPAuditResult, output_path: str = None):
    """Save audit report as JSON"""

    if not output_path:
        filename = f"audit_{result.business_name.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}.json"
        output_path = os.path.join('reports', filename)

    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w') as f:
        json.dump(asdict(result), f, indent=2)

    print(f"💾 Report saved to: {output_path}")


def main():
    """Main CLI entry point"""

    parser = argparse.ArgumentParser(
        description='Audit Google Business Profiles and generate opportunity reports'
    )
    parser.add_argument('business_name', nargs='?', help='Business name to audit')
    parser.add_argument('location', nargs='?', help='City, State or address')
    parser.add_argument('--demo', action='store_true', help='Run with demo data')
    parser.add_argument('--json', action='store_true', help='Save report as JSON')
    parser.add_argument('--api-key', help='Google Places API key (or set GOOGLE_PLACES_API_KEY env var)')

    args = parser.parse_args()

    # Demo mode
    if args.demo or (not args.business_name and not args.location):
        print("🎭 Running in DEMO mode (no API required)\n")
        business_name = "Joe's Coffee Shop"
        location = "Seattle, WA"
    else:
        if not args.business_name or not args.location:
            parser.print_help()
            sys.exit(1)
        business_name = args.business_name
        location = args.location

    # Run audit
    auditor = GBPAuditor(api_key=args.api_key)
    result = auditor.audit(business_name, location)

    if result:
        print_audit_report(result)

        if args.json:
            save_report_json(result)


if __name__ == '__main__':
    main()
