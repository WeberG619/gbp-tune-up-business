#!/usr/bin/env python3
"""
API Setup Helper
Guides you through setting up Google Places API for REAL data
"""

import os
from pathlib import Path

def main():
    print("=" * 70)
    print("🔑 GOOGLE PLACES API SETUP")
    print("=" * 70)
    print()
    print("You're currently using DEMO mode (fake businesses).")
    print("To get REAL businesses, you need a Google Places API key.")
    print()
    print("📚 STEP-BY-STEP GUIDE:")
    print()
    print("1. Go to: https://console.cloud.google.com/")
    print("   - Sign in with your Google account")
    print()
    print("2. Create a new project:")
    print("   - Click 'Select a project' → 'New Project'")
    print("   - Name it: 'GBP Business'")
    print("   - Click 'Create'")
    print()
    print("3. Enable Places API:")
    print("   - In the search bar, type 'Places API'")
    print("   - Click on 'Places API'")
    print("   - Click 'Enable'")
    print()
    print("4. Create API Key:")
    print("   - Go to 'Credentials' (left sidebar)")
    print("   - Click 'Create Credentials' → 'API Key'")
    print("   - Copy your API key (starts with AIzaSy...)")
    print()
    print("5. Set up billing (FREE tier):")
    print("   - Google requires a credit card for verification")
    print("   - BUT: First $200/month is FREE")
    print("   - That's ~40,000 searches per month")
    print("   - You'll use ~200 searches for this project")
    print("   - Cost: $0 (unless you search 40,000+ times)")
    print()
    print("=" * 70)
    print()

    # Check if .env exists
    env_file = Path('.env')

    if env_file.exists():
        print("✅ .env file already exists")
        with open(env_file, 'r') as f:
            content = f.read()
            if 'GOOGLE_PLACES_API_KEY' in content:
                print("✅ GOOGLE_PLACES_API_KEY is set")
            else:
                print("⚠️  GOOGLE_PLACES_API_KEY not found in .env")
    else:
        print("⚠️  No .env file found")

    print()
    response = input("Do you have your Google API key ready? (y/n): ").lower()

    if response == 'y':
        api_key = input("Paste your API key here: ").strip()

        if not api_key:
            print("❌ No API key provided")
            return

        print()
        your_name = input("Your name: ").strip() or "Your Name"
        your_phone = input("Your phone: ").strip() or "(555) 123-4567"
        your_email = input("Your email: ").strip() or "you@example.com"

        # Create .env file
        with open('.env', 'w') as f:
            f.write(f"GOOGLE_PLACES_API_KEY={api_key}\n")
            f.write(f"YOUR_NAME={your_name}\n")
            f.write(f"YOUR_PHONE={your_phone}\n")
            f.write(f"YOUR_EMAIL={your_email}\n")

        print()
        print("=" * 70)
        print("✅ API KEY SAVED!")
        print("=" * 70)
        print()
        print("🎯 Now run this to get REAL data:")
        print()
        print("python3 tools/market_mapper.py \\")
        print("  --locations 'Sandpoint, ID' 'Coeur d\\'Alene, ID' 'Spokane, WA' \\")
        print("  --industries 'coffee shop' 'salon' 'gym' 'restaurant' \\")
        print("  --limit 20")
        print()
        print("This will find REAL businesses with actual:")
        print("  • Real phone numbers")
        print("  • Real addresses")
        print("  • Real reviews")
        print("  • Real photos counts")
        print()
    else:
        print()
        print("No problem! Follow the steps above to get your API key.")
        print()
        print("🔗 Direct link: https://console.cloud.google.com/apis/credentials")
        print()
        print("After you get your key, run this script again:")
        print("  python3 setup_api.py")
        print()

if __name__ == '__main__':
    main()
