#!/usr/bin/env python3
"""
Email Finder - Automatically find business email addresses from websites

Scrapes business websites to find contact emails automatically.
Works with the lead data from market_mapper.py

Usage:
    python3 tools/email_finder.py --csv maps/market_leads_*.csv
    python3 tools/email_finder.py --business "Sand Creek Salon" --website "https://example.com"
"""

import os
import sys
import csv
import re
import requests
from bs4 import BeautifulSoup
from pathlib import Path
import time
import argparse
from urllib.parse import urljoin, urlparse


class EmailFinder:
    """Find email addresses from business websites"""

    def __init__(self):
        self.email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })

    def find_emails_on_page(self, url, timeout=10):
        """Find all email addresses on a webpage"""
        try:
            response = self.session.get(url, timeout=timeout)
            response.raise_for_status()

            # Parse HTML
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find emails in text
            text_emails = self.email_pattern.findall(response.text)

            # Find emails in mailto links
            mailto_emails = []
            for link in soup.find_all('a', href=True):
                if link['href'].startswith('mailto:'):
                    email = link['href'].replace('mailto:', '').split('?')[0]
                    mailto_emails.append(email)

            # Combine and deduplicate
            all_emails = list(set(text_emails + mailto_emails))

            # Filter out common non-business emails
            filtered_emails = [
                email for email in all_emails
                if not any(x in email.lower() for x in ['example.com', 'test.com', 'domain.com', 'yoursite.com'])
            ]

            return filtered_emails

        except Exception as e:
            return []

    def find_contact_page(self, base_url):
        """Try to find contact page URL"""
        contact_keywords = ['contact', 'about', 'reach-us', 'get-in-touch']

        try:
            response = self.session.get(base_url, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')

            # Look for contact page links
            for link in soup.find_all('a', href=True):
                href = link['href'].lower()
                text = link.get_text().lower()

                if any(keyword in href or keyword in text for keyword in contact_keywords):
                    full_url = urljoin(base_url, link['href'])
                    return full_url

        except:
            pass

        return None

    def find_email_for_business(self, business_name, website_url):
        """Find email for a specific business"""

        if not website_url or website_url == '':
            return None

        print(f"  🔍 Searching for email at {website_url}")

        # Try homepage first
        emails = self.find_emails_on_page(website_url)

        if emails:
            print(f"    ✓ Found: {emails[0]}")
            return emails[0]

        # Try contact page
        contact_url = self.find_contact_page(website_url)
        if contact_url:
            print(f"  🔍 Checking contact page...")
            emails = self.find_emails_on_page(contact_url)

            if emails:
                print(f"    ✓ Found: {emails[0]}")
                return emails[0]

        print(f"    ✗ No email found")
        return None

    def process_leads_csv(self, csv_file, output_file=None):
        """Process leads CSV and find emails for each business"""

        csv_path = Path(csv_file)
        if not csv_path.exists():
            print(f"❌ File not found: {csv_file}")
            return

        # Read leads
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            leads = list(reader)

        print(f"📊 Processing {len(leads)} businesses...")
        print()

        # Find emails
        for i, lead in enumerate(leads, 1):
            business = lead.get('business_name', 'Unknown')
            website = lead.get('website', '')

            if lead.get('email'):
                print(f"{i}. {business}")
                print(f"    ✓ Email already set: {lead['email']}")
                continue

            print(f"{i}. {business}")

            if not website or website == '':
                print(f"    ⚠️  No website listed")
                lead['email'] = ''
                continue

            # Find email
            email = self.find_email_for_business(business, website)
            lead['email'] = email or ''

            # Rate limiting
            time.sleep(2)  # Be polite to websites

        # Save updated CSV
        if not output_file:
            output_file = csv_path.parent / f"{csv_path.stem}_with_emails.csv"

        # Write updated leads
        fieldnames = list(leads[0].keys())
        if 'email' not in fieldnames:
            fieldnames.append('email')

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(leads)

        print()
        print("=" * 60)
        print(f"✅ Saved to: {output_file}")
        print()

        # Summary
        emails_found = sum(1 for lead in leads if lead.get('email'))
        print(f"📊 SUMMARY:")
        print(f"   Total businesses: {len(leads)}")
        print(f"   Emails found: {emails_found}")
        print(f"   No email: {len(leads) - emails_found}")
        print()

        return output_file


def main():
    parser = argparse.ArgumentParser(
        description='Find email addresses from business websites'
    )
    parser.add_argument('--csv', help='CSV file with leads')
    parser.add_argument('--business', help='Business name')
    parser.add_argument('--website', help='Business website URL')
    parser.add_argument('--output', help='Output CSV file')

    args = parser.parse_args()

    finder = EmailFinder()

    if args.csv:
        finder.process_leads_csv(args.csv, args.output)
    elif args.business and args.website:
        email = finder.find_email_for_business(args.business, args.website)
        if email:
            print(f"✓ Email: {email}")
        else:
            print("✗ No email found")
    else:
        print("Usage:")
        print("  Find emails for all leads:")
        print("    python3 tools/email_finder.py --csv maps/market_leads_*.csv")
        print()
        print("  Find email for single business:")
        print("    python3 tools/email_finder.py --business 'Business Name' --website 'https://example.com'")


if __name__ == '__main__':
    main()
