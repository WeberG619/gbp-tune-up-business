#!/usr/bin/env python3
"""
Email Campaign Tool - Send professional outreach emails to leads with email addresses

Usage:
    python email_campaign.py --csv maps/market_leads_20251030_214319_with_emails.csv --template 1
"""

import os
import sys
import csv
import argparse
from datetime import datetime
from typing import List, Dict
import time

# Email templates
EMAIL_TEMPLATES = {
    1: {
        "subject": "{business_name} - Your Google Profile is Missing Customers",
        "body": """Hi {contact_name},

I was researching local {industry} businesses in {location} and came across {business_name}.

I pulled up your Google Business Profile and noticed a few things that are probably costing you customers:

{reasons}

The problem: Google shows complete profiles FIRST - even to people searching right next to you. Incomplete = invisible.

I help North Idaho businesses fix this in 90 minutes:
• 20 professional photos (exterior, interior, products, team)
• Complete profile optimization (all info fields)
• 4 weeks of scheduled posts
• 10 pre-answered Q&As
• Review reply templates

One-time cost: $179
Guarantee: More calls within 14 days or full refund

I've attached a free audit report showing exactly what's missing from your profile and how you compare to competitors.

Want to see it? Just reply "yes" and I'll send it over.

Best regards,
Visible Local
contact@visiblelocal.co
North Idaho

P.S. I'm local to North Idaho and can usually start within 1-2 days."""
    },

    2: {
        "subject": "Quick Question About {business_name}'s Google Listing",
        "body": """Hi there,

I noticed {business_name} on Google Maps today while researching local {industry} businesses.

Quick question: Are you actively trying to get more customers through your Google Business Profile?

I ask because I spotted a few quick wins:
{reasons}

Most business owners don't realize that Google ranks complete profiles 3X higher than incomplete ones.

I specialize in fixing this - takes 90 minutes, costs $179, and businesses typically see more calls within the first week.

If you're interested in a free audit showing exactly what's missing, just let me know. No pressure if not!

Cheers,
Visible Local
contact@visiblelocal.co
North Idaho"""
    },

    3: {
        "subject": "Free Google Profile Audit for {business_name}",
        "body": """Hi,

I run a Google Business Profile optimization service in North Idaho, and I'm offering free audits to {industry} businesses this week.

I took a quick look at {business_name}'s profile and found some opportunities:

{reasons}

If you're interested, I can send you a detailed audit report (free, no obligation) showing:
✓ Your current profile score vs. competitors
✓ Exactly what's missing
✓ Estimated impact on calls/traffic

Just reply "send it" and I'll email it over.

If not interested, no worries - I won't bug you again!

Best,
Visible Local
contact@visiblelocal.co
North Idaho"""
    },

    4: {
        "subject": "Local business owner here - noticed {business_name}'s Google listing",
        "body": """Hey,

I run Visible Local and help North Idaho businesses get more customers through Google.

I was checking out {business_name} and noticed your Google profile could use some work:

{reasons}

What I do:
• Professional photos (20+)
• Complete profile optimization
• Weekly posts + review management
• $179 one-time or $59/mo ongoing

Most businesses see noticeably more calls within the first month.

Interested? Reply and I'll send a free audit showing exactly what's missing.

Thanks,
Visible Local
contact@visiblelocal.co
North Idaho"""
    },

    5: {
        "subject": "Is Google Sending You Enough Customers?",
        "body": """Hi,

Simple question: How many new customers are you getting through Google each month?

Most {industry} businesses I talk to say "not many" or "I don't know."

That's usually because their Google Business Profile is incomplete - which hurts their ranking.

I checked out {business_name} and found these gaps:
{reasons}

Good news: This is easy to fix. Takes 90 minutes, costs $179, and you'll see results within days.

Want a free audit showing your current score vs. competitors?

Reply "yes" and I'll send it over.

Best regards,
Visible Local
contact@visiblelocal.co
North Idaho"""
    }
}

def load_leads_with_emails(csv_path: str) -> List[Dict]:
    """Load leads that have email addresses"""
    leads = []

    with open(csv_path, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get('email') and row['email'].strip() and '@' in row['email']:
                # Skip generic/placeholder emails
                if row['email'] in ['filler@godaddy.com', 'webreporting@gargle.com']:
                    continue
                leads.append(row)

    return leads

def format_email(template_id: int, lead: Dict) -> Dict[str, str]:
    """Format email with lead data"""
    template = EMAIL_TEMPLATES[template_id]

    # Extract contact name from business name (or use generic)
    business_name = lead['business_name']
    contact_name = business_name.split()[0] if business_name else "there"

    # Format reasons
    reasons_list = lead.get('reasons', '').split('; ')
    reasons = '\n'.join([f"• {reason}" for reason in reasons_list if reason])

    # Format email
    subject = template['subject'].format(
        business_name=business_name,
        industry=lead.get('industry', 'business'),
        location=lead.get('location', 'your area')
    )

    body = template['body'].format(
        business_name=business_name,
        contact_name=contact_name,
        industry=lead.get('industry', 'business'),
        location=lead.get('location', ''),
        reasons=reasons
    )

    return {
        'to': lead['email'],
        'subject': subject,
        'body': body,
        'business_name': business_name,
        'phone': lead.get('phone', '')
    }

def preview_emails(leads: List[Dict], template_id: int, count: int = 3):
    """Preview first N emails"""
    print(f"\n{'=' * 80}")
    print(f"📧 EMAIL PREVIEW (Template #{template_id})")
    print(f"{'=' * 80}\n")

    for i, lead in enumerate(leads[:count], 1):
        email = format_email(template_id, lead)

        print(f"Email {i}/{count}")
        print(f"To: {email['to']}")
        print(f"Subject: {email['subject']}")
        print(f"\n{email['body']}\n")
        print("-" * 80)

    print(f"\n✅ {len(leads)} total emails ready to send\n")

def export_emails_to_csv(leads: List[Dict], template_id: int, output_path: str):
    """Export formatted emails to CSV for mail merge"""
    os.makedirs(os.path.dirname(output_path) or '.', exist_ok=True)

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['email', 'business_name', 'subject', 'body', 'phone', 'industry', 'location']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for lead in leads:
            email = format_email(template_id, lead)
            writer.writerow({
                'email': email['to'],
                'business_name': email['business_name'],
                'subject': email['subject'],
                'body': email['body'],
                'phone': email['phone'],
                'industry': lead.get('industry', ''),
                'location': lead.get('location', '')
            })

    print(f"✅ Exported {len(leads)} emails to: {output_path}")
    print(f"\n📤 NEXT STEPS:")
    print(f"1. Import {output_path} into Gmail, Mailchimp, or GMass")
    print(f"2. Use mail merge to send personalized emails")
    print(f"3. Track responses")

def main():
    parser = argparse.ArgumentParser(
        description='Email campaign tool for Visible Local'
    )
    parser.add_argument('--csv', required=True, help='CSV file with leads (must have email column)')
    parser.add_argument('--template', type=int, default=1, choices=[1,2,3,4,5],
                       help='Email template to use (1-5)')
    parser.add_argument('--preview', type=int, default=3,
                       help='Number of emails to preview (default: 3)')
    parser.add_argument('--export', action='store_true',
                       help='Export to CSV for mail merge')
    parser.add_argument('--output', default=None,
                       help='Output file path (default: email_campaign_YYYYMMDD.csv)')

    args = parser.parse_args()

    # Load leads
    print(f"\n📊 Loading leads from: {args.csv}")
    leads = load_leads_with_emails(args.csv)

    if not leads:
        print("❌ No leads with valid email addresses found")
        sys.exit(1)

    print(f"✅ Found {len(leads)} leads with email addresses\n")

    # Preview emails
    preview_emails(leads, args.template, args.preview)

    # Export if requested
    if args.export:
        if not args.output:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            args.output = f'email_campaigns/campaign_template{args.template}_{timestamp}.csv'

        export_emails_to_csv(leads, args.template, args.output)
        print(f"\n💡 TIP: Use GMass (gmass.co) for Gmail mail merge - it's free for up to 50 emails/day")

    # Show template info
    print(f"\n📋 TEMPLATE #{args.template} INFO:")
    print(f"Subject: {EMAIL_TEMPLATES[args.template]['subject']}")
    print(f"\nBest for:")
    if args.template == 1:
        print("• First contact with detailed value prop")
        print("• Professional, direct approach")
    elif args.template == 2:
        print("• Casual, question-based opener")
        print("• Lower pressure")
    elif args.template == 3:
        print("• Lead with free value (audit)")
        print("• Good for cold outreach")
    elif args.template == 4:
        print("• Local angle, personal touch")
        print("• Time-limited offer")
    elif args.template == 5:
        print("• Results-focused")
        print("• Good for skeptical prospects")

    print("\n🚀 Ready to send!")

if __name__ == '__main__':
    main()
