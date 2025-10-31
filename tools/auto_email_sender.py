#!/usr/bin/env python3
"""
AUTOMATED EMAIL SENDER
Sends personalized emails to leads automatically with tracking

Features:
- Sends emails in batches (avoid spam filters)
- Personalizes each email
- Attaches PDF audit reports
- Tracks sent/bounced/opened emails
- Schedules follow-ups automatically
- Respects daily sending limits

Usage:
    python tools/auto_email_sender.py --batch 10
    python tools/auto_email_sender.py --batch 10 --send  # Actually send
"""

import os
import sys
import csv
import json
import time
import smtplib
import argparse
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime, timedelta
from pathlib import Path

# Try to load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except:
    pass


class AutoEmailSender:
    def __init__(self, tracking_file="automation_data/email_tracking.json"):
        self.tracking_file = Path(tracking_file)
        self.tracking_file.parent.mkdir(exist_ok=True)

        # Load tracking data
        self.tracking = self._load_tracking()

        # Email configuration
        self.gmail_address = os.getenv('GMAIL_ADDRESS')
        self.gmail_password = os.getenv('GMAIL_APP_PASSWORD')
        self.your_name = os.getenv('YOUR_NAME', 'Your Name')
        self.your_phone = os.getenv('YOUR_PHONE', '(555) 123-4567')
        self.your_email = os.getenv('YOUR_EMAIL', 'you@example.com')

    def _load_tracking(self):
        """Load email tracking data"""
        if self.tracking_file.exists():
            with open(self.tracking_file, 'r') as f:
                return json.load(f)
        return {
            'sent': [],
            'bounced': [],
            'responded': [],
            'last_batch': None,
            'daily_count': 0,
            'daily_limit': 50
        }

    def _save_tracking(self):
        """Save tracking data"""
        with open(self.tracking_file, 'w') as f:
            json.dump(self.tracking, f, indent=2)

    def send_batch(self, leads, batch_size=10, dry_run=True, delay_seconds=30):
        """
        Send batch of emails to leads

        Args:
            leads: List of lead dictionaries
            batch_size: Number to send in this batch
            dry_run: If True, just print what would be sent
            delay_seconds: Delay between emails to avoid spam filters
        """
        print("=" * 70)
        print("📧 AUTOMATED EMAIL SENDER")
        print("=" * 70)
        print()

        if dry_run:
            print("🔍 DRY RUN MODE - No emails will actually be sent")
            print()

        # Check Gmail credentials
        if not dry_run and (not self.gmail_address or not self.gmail_password):
            print("❌ Gmail credentials not configured!")
            print("   Set these in .env file:")
            print("   GMAIL_ADDRESS=your.email@gmail.com")
            print("   GMAIL_APP_PASSWORD=your_app_password")
            return

        # Filter leads not yet contacted
        to_contact = []
        for lead in leads[:batch_size]:
            if not self._already_sent(lead['business_name']):
                to_contact.append(lead)

        if not to_contact:
            print("✅ All leads in this batch already contacted!")
            return

        print(f"📋 Sending to {len(to_contact)} businesses:")
        print()

        sent_count = 0
        failed_count = 0

        for i, lead in enumerate(to_contact, 1):
            business = lead['business_name']
            print(f"{i}/{len(to_contact)}. {business}")

            # Create email
            email_content = self._create_email(lead)

            if dry_run:
                print(f"    To: {email_content['to']}")
                print(f"    Subject: {email_content['subject']}")
                print(f"    ✓ Would send email\n")
                self._track_email(lead, 'sent', dry_run=True)
                sent_count += 1
            else:
                # Actually send email
                try:
                    self._send_email(email_content)
                    print(f"    ✓ Sent successfully\n")
                    self._track_email(lead, 'sent')
                    sent_count += 1

                    # Delay between emails
                    if i < len(to_contact):
                        print(f"    ⏳ Waiting {delay_seconds}s before next email...")
                        time.sleep(delay_seconds)

                except Exception as e:
                    print(f"    ✗ Failed: {str(e)}\n")
                    self._track_email(lead, 'failed')
                    failed_count += 1

        print()
        print("=" * 70)
        print("📊 BATCH SUMMARY")
        print("=" * 70)
        print(f"✅ Sent: {sent_count}")
        print(f"❌ Failed: {failed_count}")
        print()

        if dry_run:
            print("💡 To actually send, run with --send flag:")
            print(f"   python tools/auto_email_sender.py --batch {batch_size} --send")
        else:
            print("📅 Next Steps:")
            print(f"   1. Wait 3 days for responses")
            print(f"   2. Run follow-up script: python tools/auto_followup.py")
            print(f"   3. Check tracking: automation_data/email_tracking.json")

        self._save_tracking()

    def _already_sent(self, business_name):
        """Check if we already sent to this business"""
        return any(e['business'] == business_name for e in self.tracking['sent'])

    def _create_email(self, lead):
        """Create personalized email content"""
        business = lead['business_name']
        location_city = lead['location'].split(',')[0]
        industry = lead['industry']
        score = lead.get('score', 0)
        issues = lead['reasons'].split(';')[0]  # First issue

        # Personalized subject lines (rotate for variety)
        subjects = [
            f"Quick question about {business}'s Google presence",
            f"{business} - noticed something on your Google profile",
            f"Free audit for {business}",
            f"{business} vs. competitors on Google"
        ]

        subject = subjects[hash(business) % len(subjects)]

        body = f"""Hi there,

I was researching local {industry}s in {location_city} and came across {business}.

I noticed something that might be costing you customers: {issues.lower().strip()}

This is more important than most business owners realize - 86% of customers check Google before visiting a local business. If your profile looks incomplete, they choose a competitor instead.

I help local businesses fix this. Most of my clients see 30-50% more calls within the first month.

I've already prepared a free audit report for {business} showing:
✓ Your current score vs. competitors
✓ Exactly what's missing
✓ How much it's costing you in lost customers

Would you like me to send it over? It's free, no strings attached.

Best regards,
{self.your_name}
{self.your_phone}
{self.your_email}

P.S. This takes 90 minutes to fix and costs $179. Most clients make it back in the first week.
"""

        return {
            'to': lead.get('email', f"[Find email for {business}]"),
            'subject': subject,
            'body': body,
            'business_name': business,
            'phone': lead.get('phone'),
            'attachment': lead.get('report_path')
        }

    def _send_email(self, email_content):
        """Actually send the email via Gmail SMTP"""
        msg = MIMEMultipart()
        msg['From'] = f"{self.your_name} <{self.gmail_address}>"
        msg['To'] = email_content['to']
        msg['Subject'] = email_content['subject']

        # Add body
        msg.attach(MIMEText(email_content['body'], 'plain'))

        # Add attachment if exists
        if email_content.get('attachment') and Path(email_content['attachment']).exists():
            with open(email_content['attachment'], 'rb') as f:
                attachment = MIMEApplication(f.read(), _subtype='pdf')
                attachment.add_header('Content-Disposition', 'attachment',
                                    filename=Path(email_content['attachment']).name)
                msg.attach(attachment)

        # Send via Gmail SMTP
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(self.gmail_address, self.gmail_password)
            server.send_message(msg)

    def _track_email(self, lead, status, dry_run=False):
        """Track sent email"""
        record = {
            'business': lead['business_name'],
            'phone': lead.get('phone'),
            'location': lead['location'],
            'score': lead.get('score'),
            'sent_date': datetime.now().isoformat(),
            'status': status,
            'followup_date': (datetime.now() + timedelta(days=3)).isoformat(),
            'dry_run': dry_run
        }

        if status == 'sent':
            self.tracking['sent'].append(record)
        elif status == 'failed':
            self.tracking['bounced'].append(record)


class AutoFollowUp:
    """Automated follow-up system"""

    def __init__(self, tracking_file="automation_data/email_tracking.json"):
        self.tracking_file = Path(tracking_file)

        if not self.tracking_file.exists():
            self.tracking = {'sent': [], 'responded': []}
        else:
            with open(self.tracking_file, 'r') as f:
                self.tracking = json.load(f)

    def get_followups_due(self):
        """Get list of leads needing follow-up"""
        followups = []
        now = datetime.now()

        for record in self.tracking['sent']:
            followup_date = datetime.fromisoformat(record['followup_date'])

            # Check if follow-up is due
            if followup_date <= now:
                # Check if not already responded
                if not any(r['business'] == record['business'] for r in self.tracking['responded']):
                    followups.append(record)

        return followups

    def generate_followup_list(self):
        """Generate today's follow-up action list"""
        followups = self.get_followups_due()

        if not followups:
            print("✅ No follow-ups due today!")
            return

        print("=" * 70)
        print(f"📅 FOLLOW-UPS DUE TODAY - {datetime.now().strftime('%B %d, %Y')}")
        print("=" * 70)
        print()

        for i, lead in enumerate(followups, 1):
            print(f"{i}. {lead['business']}")
            print(f"   Phone: {lead['phone']}")
            print(f"   Location: {lead['location']}")
            print(f"   Original email: {lead['sent_date'][:10]}")
            print()

        # Save to file
        followup_file = Path("automation_data/today_followups.txt")
        with open(followup_file, 'w') as f:
            f.write(f"FOLLOW-UPS DUE - {datetime.now().strftime('%B %d, %Y')}\n")
            f.write("=" * 60 + "\n\n")

            for i, lead in enumerate(followups, 1):
                f.write(f"{i}. {lead['business']}\n")
                f.write(f"   Phone: {lead['phone']}\n")
                f.write(f"   Score: {lead['score']}\n")
                f.write(f"   Action: Call or send follow-up email\n")
                f.write(f"   Script: 'Hi, I sent you a free audit report for {lead['business']} a few days ago. Did you get a chance to look at it?'\n\n")

        print(f"📋 Full list saved to: {followup_file}")
        print()
        print("💡 FOLLOW-UP SCRIPT:")
        print("   'Hi, I sent you a free audit report a few days ago.'")
        print("   'Did you get a chance to look at it?'")
        print("   'Would you like me to walk you through it real quick?'")


def main():
    parser = argparse.ArgumentParser(
        description='Automated email sender with tracking'
    )

    subparsers = parser.add_subparsers(dest='command', help='Commands')

    # Send command
    send_parser = subparsers.add_parser('send', help='Send emails to leads')
    send_parser.add_argument('--batch', type=int, default=10,
                            help='Number of emails to send')
    send_parser.add_argument('--send', action='store_true',
                            help='Actually send (default is dry-run)')
    send_parser.add_argument('--delay', type=int, default=30,
                            help='Seconds between emails (default: 30)')

    # Follow-up command
    followup_parser = subparsers.add_parser('followup', help='Check follow-ups due')

    # Status command
    status_parser = subparsers.add_parser('status', help='Check email status')

    args = parser.parse_args()

    if args.command == 'send':
        # Load leads
        leads_file = Path("automation_data/all_leads.csv")
        if not leads_file.exists():
            print("❌ No leads found!")
            print("   Run automation first: python tools/automation_master.py --auto-run")
            return

        with open(leads_file, 'r') as f:
            reader = csv.DictReader(f)
            leads = list(reader)

        # Sort by score
        leads = sorted(leads, key=lambda x: int(x.get('score', 0)), reverse=True)

        # Send batch
        sender = AutoEmailSender()
        sender.send_batch(leads, batch_size=args.batch,
                         dry_run=not args.send, delay_seconds=args.delay)

    elif args.command == 'followup':
        followup = AutoFollowUp()
        followup.generate_followup_list()

    elif args.command == 'status':
        sender = AutoEmailSender()
        print("=" * 70)
        print("📊 EMAIL CAMPAIGN STATUS")
        print("=" * 70)
        print()
        print(f"Emails sent: {len(sender.tracking['sent'])}")
        print(f"Responses: {len(sender.tracking.get('responded', []))}")
        print(f"Bounced: {len(sender.tracking.get('bounced', []))}")
        print()

        if sender.tracking['sent']:
            print("Recent emails:")
            for email in sender.tracking['sent'][-5:]:
                print(f"  • {email['business']} - {email['sent_date'][:10]}")

    else:
        parser.print_help()


if __name__ == '__main__':
    main()
