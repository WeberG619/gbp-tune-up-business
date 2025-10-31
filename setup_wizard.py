#!/usr/bin/env python3
"""
Setup Wizard - Configure your GBP business in 5 minutes

This script helps you:
1. Set your contact information
2. Configure API keys (optional)
3. Test all tools
4. Generate your first reports
"""

import os
import sys
import subprocess
from pathlib import Path


def print_header(text):
    print("\n" + "=" * 60)
    print(f"  {text}")
    print("=" * 60 + "\n")


def print_step(number, text):
    print(f"\n{'─' * 60}")
    print(f"STEP {number}: {text}")
    print('─' * 60 + "\n")


def get_input(prompt, default=""):
    """Get user input with optional default"""
    if default:
        response = input(f"{prompt} [{default}]: ").strip()
        return response if response else default
    return input(f"{prompt}: ").strip()


def confirm(prompt):
    """Get yes/no confirmation"""
    response = input(f"{prompt} (y/n): ").lower().strip()
    return response == 'y' or response == 'yes'


def main():
    print_header("🚀 GBP Business Setup Wizard")

    print("This wizard will configure your business in 5 minutes.")
    print("You can skip anything and come back later.\n")

    if not confirm("Ready to start?"):
        print("Come back when you're ready!")
        return

    # Step 1: Contact Information
    print_step(1, "Your Contact Information")

    print("This information will appear on:")
    print("  • PDF audit reports")
    print("  • Email templates")
    print("  • Landing page")
    print("  • Invoices\n")

    your_name = get_input("Your full name", "John Smith")
    your_business = get_input("Business name (or just your name)", your_name)
    your_phone = get_input("Phone number", "(555) 123-4567")
    your_email = get_input("Email address", "you@example.com")
    your_city = get_input("Your city", "Austin")
    your_state = get_input("Your state (2 letters)", "TX")

    # Step 2: Payment Methods
    print_step(2, "Payment Methods")

    print("How will clients pay you?\n")

    payment_methods = []

    if confirm("Do you have Venmo?"):
        venmo = get_input("Venmo username (with @)", "@yourname")
        payment_methods.append(f"Venmo: {venmo}")

    if confirm("Do you have Zelle?"):
        zelle = get_input("Zelle email or phone", your_email)
        payment_methods.append(f"Zelle: {zelle}")

    if confirm("Do you have PayPal?"):
        paypal = get_input("PayPal email", your_email)
        payment_methods.append(f"PayPal: {paypal}")

    if confirm("Can you accept cash?"):
        payment_methods.append("Cash")

    if not payment_methods:
        print("\n⚠️  You should set up at least ONE payment method!")
        print("Venmo and Zelle are free and easy. Set one up now:\n")
        print("  Venmo: https://venmo.com/")
        print("  Zelle: Check your banking app\n")

    # Step 3: Google API (Optional)
    print_step(3, "Google API Key (OPTIONAL)")

    print("Google API key lets you get REAL business data.")
    print("Without it, you'll use demo/fake data.\n")
    print("Cost: FREE for up to 28,000 requests/month")
    print("Setup time: 10 minutes")
    print("Guide: docs/API_SETUP_GUIDE.md\n")

    api_key = ""
    if confirm("Do you have a Google API key?"):
        api_key = get_input("Paste your API key here")
        if api_key and not api_key.startswith("AIza"):
            print("⚠️  That doesn't look like a valid API key (should start with 'AIza')")
            if not confirm("Use it anyway?"):
                api_key = ""

    # Step 4: Create .env file
    print_step(4, "Creating Configuration Files")

    env_content = f"""# Google Places API Key (optional - use demo mode without this)
GOOGLE_PLACES_API_KEY={api_key if api_key else 'your_api_key_here'}

# Your Contact Information (used in reports and templates)
YOUR_NAME={your_name}
YOUR_BUSINESS={your_business}
YOUR_PHONE={your_phone}
YOUR_EMAIL={your_email}
YOUR_CITY={your_city}
YOUR_STATE={your_state}

# Payment Methods
PAYMENT_METHODS={'; '.join(payment_methods) if payment_methods else 'Not configured yet'}
"""

    with open('.env', 'w') as f:
        f.write(env_content)

    print("✅ Created .env file with your configuration")

    # Create config file for easy access
    config_content = f"""# Quick Reference - Your Business Configuration

Your Name: {your_name}
Business: {your_business}
Phone: {your_phone}
Email: {your_email}
City: {your_city}, {your_state}

Payment Methods:
"""
    for method in payment_methods:
        config_content += f"  - {method}\n"

    if not payment_methods:
        config_content += "  - None configured yet\n"

    config_content += f"""
Google API: {'Configured ✅' if api_key else 'Not configured (using demo mode)'}

To update this information, run: python setup_wizard.py
"""

    with open('MY_CONFIG.txt', 'w') as f:
        f.write(config_content)

    print("✅ Created MY_CONFIG.txt for quick reference")

    # Step 5: Test the tools
    print_step(5, "Testing Your Setup")

    print("Let's test that everything works!\n")

    if confirm("Generate a test audit report?"):
        print("\nGenerating test report...")

        cmd = [
            'python', 'tools/gbp_audit.py',
            '--demo',
            '--your-name', your_name,
            '--your-phone', your_phone,
            '--your-email', your_email
        ]

        try:
            subprocess.run(cmd, check=True)
            print("\n✅ Test report generated! Check the reports/ folder.")
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Make sure you ran: pip install -r requirements.txt")

    # Step 6: Next steps
    print_step(6, "You're All Set!")

    print("✅ Configuration complete!\n")

    print("YOUR NEXT STEPS:\n")

    if not api_key:
        print("1. 📝 OPTIONAL: Get Google API key")
        print("   Guide: docs/API_SETUP_GUIDE.md")
        print("   (Or just use demo mode for now)\n")

    if not payment_methods:
        print("2. 💰 Set up a payment method")
        print("   Easiest: Venmo or Zelle (both free)\n")

    print("3. 🎯 Find your first leads:")
    print("   python tools/lead_finder.py --demo \"Your City, ST\" --industry \"coffee shop\"\n")

    print("4. 📄 Generate audit reports:")
    print(f"   python tools/bulk_audit.py --demo --count 5 \\")
    print(f"     --your-name \"{your_name}\" \\")
    print(f"     --your-phone \"{your_phone}\"\n")

    print("5. 📧 Send emails using templates:")
    print("   See: templates/email_outreach.md\n")

    print("6. 🌐 Deploy your landing page:")
    print("   See: landing-page/README.md\n")

    print("7. 📱 Post on social media:")
    print("   See: marketing/social-media-content.md\n")

    print("\n" + "=" * 60)
    print("  💡 Full guide: GETTING_STARTED_TODAY.md")
    print("  📖 Automation: docs/AUTOMATION_GUIDE.md")
    print("=" * 60 + "\n")

    print("Good luck! 🚀\n")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled. Run again when ready!")
        sys.exit(0)
