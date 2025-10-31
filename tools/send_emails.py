#!/usr/bin/env python3
"""
Simple Email Sender - Send outreach emails with audit reports

Requirements:
    pip install python-dotenv

Usage:
    python send_emails.py leads/leads.csv --template 1

For Gmail:
    1. Enable 2-factor authentication
    2. Create app password: https://myaccount.google.com/apppasswords
    3. Add to .env: GMAIL_ADDRESS=you@gmail.com
    4. Add to .env: GMAIL_APP_PASSWORD=your_app_password
"""

import os
import sys
import csv
import smtplib
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from pathlib import Path
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv()


# Email Templates
TEMPLATES = {
    1: {
        "subject": "Quick question about {business_name}'s Google profile",
        "body": """Hi {owner_name},

I was researching local {industry} businesses in {city} this morning and came across {business_name}.

I noticed a few things about your Google Business Profile that might be costing you customers:

• You have {photo_count} photos while competitors average 20+
• {specific_issue}
• Your profile needs optimization

I put together a quick audit report for you (attached PDF). Takes 2 minutes to read.

The short version: Google shows businesses with better profiles to MORE people. Right now, potential customers might be seeing competitors before you—even though you might be closer or better.

I help local businesses fix this. Takes about 90 minutes:
✓ 20 professional photos
✓ 4 weeks of scheduled posts
✓ Complete profile optimization

$179 one-time. Most clients see more calls within 2 weeks.

Want to chat for 5 minutes? I'm available this week.

Best,
{your_name}
{your_phone}
{your_email}

P.S. Even if you're not interested, the audit report is yours to keep. It shows exactly where you stand vs. competitors.
"""
    },
    2: {
        "subject": "Did you get a chance to review the audit?",
        "body": """Hi {owner_name},

Following up on the Google Business Profile audit I sent over a few days ago.

Quick question: Did you get a chance to look at it?

I know you're busy running {business_name}, so here's the TL;DR:

Your profile is missing {missing_items}. This is probably costing you 5-10 customer calls per week.

I can fix everything in one 90-minute session for $179.

Two questions:
1. Are you seeing enough customer calls/foot traffic right now?
2. If not, would you be open to a quick 5-minute call?

I'm booking sessions for this week. Happy to squeeze you in.

Best,
{your_name}
{your_phone}
"""
    }
}


def send_email(to_email, subject, body, attachment_path=None):
    """Send email via Gmail SMTP"""

    gmail_address = os.getenv('GMAIL_ADDRESS')
    gmail_password = os.getenv('GMAIL_APP_PASSWORD')

    if not gmail_address or not gmail_password:
        print("\n❌ Gmail not configured!")
        print("\nTo send emails, add to your .env file:")
        print("GMAIL_ADDRESS=your.email@gmail.com")
        print("GMAIL_APP_PASSWORD=your_app_password")
        print("\nGet app password: https://myaccount.google.com/apppasswords")
        return False

    # Create message
    msg = MIMEMultipart()
    msg['From'] = gmail_address
    msg['To'] = to_email
    msg['Subject'] = subject

    # Add body
    msg.attach(MIMEText(body, 'plain'))

    # Add attachment if provided
    if attachment_path and os.path.exists(attachment_path):
        with open(attachment_path, 'rb') as f:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(f.read())

        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename={Path(attachment_path).name}'
        )
        msg.attach(part)

    # Send email
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(gmail_address, gmail_password)
            server.send_message(msg)
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False


def process_leads(csv_file, template_num=1, dry_run=False, limit=None):
    """Process leads from CSV and send emails"""

    if not os.path.exists(csv_file):
        print(f"❌ File not found: {csv_file}")
        return

    # Load environment
    your_name = os.getenv('YOUR_NAME', 'Your Name')
    your_phone = os.getenv('YOUR_PHONE', '(555) 123-4567')
    your_email = os.getenv('YOUR_EMAIL', 'you@example.com')

    # Get template
    if template_num not in TEMPLATES:
        print(f"❌ Template {template_num} not found")
        print(f"Available templates: {list(TEMPLATES.keys())}")
        return

    template = TEMPLATES[template_num]

    # Read leads
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        leads = list(reader)

    if limit:
        leads = leads[:limit]

    print(f"\n📧 Processing {len(leads)} leads")
    print(f"Template: #{template_num}")
    print(f"Mode: {'DRY RUN (no emails sent)' if dry_run else 'LIVE'}\n")

    if not dry_run and not confirm(f"Send {len(leads)} emails?"):
        print("Cancelled.")
        return

    sent = 0
    failed = 0

    for i, lead in enumerate(leads, 1):
        business_name = lead.get('business_name', 'Unknown Business')
        email = lead.get('email', '')

        if not email:
            print(f"[{i}/{len(leads)}] ⚠️  {business_name} - No email address")
            failed += 1
            continue

        # Find corresponding audit report PDF
        safe_name = business_name.lower().replace(' ', '_').replace("'", '')
        safe_name = ''.join(c for c in safe_name if c.isalnum() or c == '_')

        # Look for PDF in reports folder
        pdf_paths = list(Path('reports').rglob(f'*{safe_name}*.pdf'))
        attachment = str(pdf_paths[0]) if pdf_paths else None

        # Personalize template
        subject = template['subject'].format(
            business_name=business_name
        )

        body = template['body'].format(
            business_name=business_name,
            owner_name=lead.get('owner_name', 'there'),
            industry=lead.get('industry', 'business'),
            city=lead.get('city', 'your city'),
            photo_count=lead.get('photos', '3'),
            specific_issue=lead.get('reasons', 'missing information'),
            missing_items=lead.get('reasons', 'photos and posts'),
            your_name=your_name,
            your_phone=your_phone,
            your_email=your_email
        )

        print(f"[{i}/{len(leads)}] {business_name} ({email})")

        if dry_run:
            print(f"  Subject: {subject}")
            print(f"  Attachment: {attachment if attachment else 'None'}")
            sent += 1
        else:
            if send_email(email, subject, body, attachment):
                print(f"  ✅ Sent")
                sent += 1
                time.sleep(2)  # Rate limiting
            else:
                print(f"  ❌ Failed")
                failed += 1

    print(f"\n{'=' * 60}")
    print(f"📊 SUMMARY")
    print(f"{'=' * 60}")
    print(f"Total: {len(leads)}")
    print(f"✅ Sent: {sent}")
    print(f"❌ Failed: {failed}")

    if dry_run:
        print(f"\n💡 This was a DRY RUN. No emails were actually sent.")
        print(f"Remove --dry-run to send for real.")


def confirm(prompt):
    """Get yes/no confirmation"""
    response = input(f"{prompt} (y/n): ").lower().strip()
    return response == 'y' or response == 'yes'


def main():
    parser = argparse.ArgumentParser(
        description='Send outreach emails with audit reports'
    )
    parser.add_argument('csv_file', help='CSV file with leads')
    parser.add_argument('--template', type=int, default=1,
                       help='Template number (1=initial, 2=follow-up)')
    parser.add_argument('--dry-run', action='store_true',
                       help='Test without actually sending emails')
    parser.add_argument('--limit', type=int,
                       help='Limit number of emails to send')

    args = parser.parse_args()

    process_leads(args.csv_file, args.template, args.dry_run, args.limit)


if __name__ == '__main__':
    main()
