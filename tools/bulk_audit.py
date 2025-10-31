#!/usr/bin/env python3
"""
Bulk Audit Report Generator

Generate professional PDF audit reports for multiple businesses at once.
Perfect for automated outreach campaigns.

Usage:
    python bulk_audit.py leads/leads_20251031.csv
    python bulk_audit.py --demo --count 10
"""

import os
import sys
import csv
import argparse
from pathlib import Path
import time

# Import the audit tool
sys.path.insert(0, os.path.dirname(__file__))
from gbp_audit import GBPAuditor, save_report_pdf


def process_leads_csv(csv_file: str, your_name: str, your_phone: str,
                      your_email: str, delay: float = 1.0):
    """Process leads from CSV and generate audit reports"""

    if not os.path.exists(csv_file):
        print(f"❌ File not found: {csv_file}")
        return

    print(f"📂 Loading leads from: {csv_file}")

    leads = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        leads = list(reader)

    print(f"✓ Found {len(leads)} leads\n")

    # Create output directory
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    output_dir = f"reports/bulk_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    auditor = GBPAuditor()

    successful = 0
    failed = 0

    for i, lead in enumerate(leads, 1):
        business_name = lead.get('business_name', 'Unknown')
        location = lead.get('address', '')

        # Extract city/state from address if possible
        if ',' in location:
            parts = location.split(',')
            if len(parts) >= 2:
                location = ','.join(parts[-2:]).strip()

        print(f"[{i}/{len(leads)}] Generating report for: {business_name}")

        try:
            # Run audit
            result = auditor.audit(business_name, location)

            if result:
                # Generate filename
                safe_name = business_name.lower().replace(' ', '_').replace("'", '')
                safe_name = ''.join(c for c in safe_name if c.isalnum() or c == '_')
                pdf_path = os.path.join(output_dir, f"audit_{safe_name}.pdf")

                # Generate PDF
                save_report_pdf(
                    result,
                    output_path=pdf_path,
                    your_name=your_name,
                    your_phone=your_phone,
                    your_email=your_email
                )

                successful += 1
                print(f"  ✓ Saved: {pdf_path}\n")
            else:
                failed += 1
                print(f"  ✗ Failed to generate audit\n")

            # Rate limiting
            time.sleep(delay)

        except Exception as e:
            failed += 1
            print(f"  ✗ Error: {e}\n")

    # Summary
    print("=" * 60)
    print("📊 BULK AUDIT SUMMARY")
    print("=" * 60)
    print(f"Total Leads: {len(leads)}")
    print(f"✓ Successful: {successful}")
    print(f"✗ Failed: {failed}")
    print(f"\n📁 Reports saved to: {output_dir}/")
    print("\n💡 NEXT STEPS:")
    print("1. Review the generated PDF reports")
    print("2. Send personalized emails using templates/email_outreach.md")
    print("3. Attach the specific business's audit report to each email")
    print("4. Track responses in your client tracker")


def generate_demo_reports(count: int, your_name: str, your_phone: str, your_email: str):
    """Generate demo reports for testing"""

    print(f"🎭 Generating {count} demo audit reports...\n")

    # Demo businesses
    demo_businesses = [
        ("Joe's Coffee Shop", "Seattle, WA"),
        ("Bella's Hair Salon", "Austin, TX"),
        ("Quick Fix Plumbing", "Denver, CO"),
        ("Peak Performance Gym", "Portland, OR"),
        ("The Burger Joint", "San Diego, CA"),
        ("Zen Yoga Studio", "Boulder, CO"),
        ("Mike's Auto Repair", "Phoenix, AZ"),
        ("Fresh Cuts Barber", "Nashville, TN"),
        ("Downtown Dental", "Atlanta, GA"),
        ("Paws & Claws Vet", "Minneapolis, MN"),
    ]

    # Create output directory
    timestamp = time.strftime('%Y%m%d_%H%M%S')
    output_dir = f"reports/demo_bulk_{timestamp}"
    os.makedirs(output_dir, exist_ok=True)

    auditor = GBPAuditor()

    for i in range(min(count, len(demo_businesses))):
        business_name, location = demo_businesses[i]

        print(f"[{i+1}/{count}] Generating report for: {business_name}")

        # Run audit
        result = auditor.audit(business_name, location)

        if result:
            # Generate filename
            safe_name = business_name.lower().replace(' ', '_').replace("'", '')
            safe_name = ''.join(c for c in safe_name if c.isalnum() or c == '_')
            pdf_path = os.path.join(output_dir, f"audit_{safe_name}.pdf")

            # Generate PDF
            save_report_pdf(
                result,
                output_path=pdf_path,
                your_name=your_name,
                your_phone=your_phone,
                your_email=your_email
            )

            print(f"  ✓ Saved: {pdf_path}\n")

    print(f"\n✅ Generated {count} demo reports in: {output_dir}/")


def main():
    """Main CLI entry point"""

    parser = argparse.ArgumentParser(
        description='Generate bulk audit reports from leads CSV'
    )
    parser.add_argument('csv_file', nargs='?',
                       help='CSV file with leads (from lead_finder.py)')
    parser.add_argument('--demo', action='store_true',
                       help='Generate demo reports instead of from CSV')
    parser.add_argument('--count', type=int, default=10,
                       help='Number of demo reports to generate (default: 10)')
    parser.add_argument('--your-name', default='Your Name',
                       help='Your name for PDF footer')
    parser.add_argument('--your-phone', default='(555) 123-4567',
                       help='Your phone for PDF footer')
    parser.add_argument('--your-email', default='you@example.com',
                       help='Your email for PDF footer')
    parser.add_argument('--delay', type=float, default=1.0,
                       help='Delay between reports in seconds (default: 1.0)')

    args = parser.parse_args()

    if args.demo:
        generate_demo_reports(
            count=args.count,
            your_name=args.your_name,
            your_phone=args.your_phone,
            your_email=args.your_email
        )
    else:
        if not args.csv_file:
            print("❌ Error: CSV file required (or use --demo)")
            parser.print_help()
            sys.exit(1)

        process_leads_csv(
            csv_file=args.csv_file,
            your_name=args.your_name,
            your_phone=args.your_phone,
            your_email=args.your_email,
            delay=args.delay
        )


if __name__ == '__main__':
    main()
