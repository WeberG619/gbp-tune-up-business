# ✅ PRE-FLIGHT CHECKLIST

**Before you can actually get a paying customer, you MUST complete these items.**

This checklist tells you exactly what's missing and how to fix it.

---

## 🔴 CRITICAL (Can't get customers without these)

### 1. Contact Information Configured

**Why:** Your PDFs/emails say "[YOUR NAME]" right now - looks fake

**Status:** ❌ NOT DONE

**How to fix (2 minutes):**
```bash
python setup_wizard.py
```

**Or manually:**
- Edit `.env` file
- Replace all `[YOUR NAME]`, `[YOUR PHONE]`, `[YOUR EMAIL]`

**Test:**
```bash
python tools/gbp_audit.py --demo --your-name "Your Name"
# Check PDF footer has YOUR actual info
```

---

### 2. Payment Method Set Up

**Why:** Clients need a way to pay you

**Status:** ❌ NOT DONE

**Options (pick ONE):**
- **Venmo** (Easiest) - Download app, create account
- **Zelle** (Free) - Built into most banking apps
- **Cash** (Works) - Just bring change
- **PayPal** - paypal.com/business
- **Square** - squareup.com (2.6% + 10¢ fee)

**Minimum:** Set up Venmo OR Zelle (both are FREE and instant)

---

### 3. Way to Find Real Leads

**Current problem:** Lead finder gives FAKE businesses without API

**Solutions:**

#### Option A: Get Google API Key (Best - FREE)
**Time:** 10 minutes
**Cost:** FREE (28,000 requests/month)
**Guide:** `docs/API_SETUP_GUIDE.md`

```bash
# After setup:
python tools/lead_finder.py "Your City, ST" --industry "salon" --limit 20
# Returns REAL businesses with real contact info
```

#### Option B: Manual Google Maps Search (Works Now)
**Time:** 30 minutes
**Cost:** $0

1. Open Google Maps
2. Search "coffee shop [your city]"
3. Look for businesses with:
   - 3-10 photos (low)
   - Few reviews (3-20)
   - No recent posts
4. Write down:
   - Business name
   - Address
   - Phone (if shown)
   - Website (if shown)
5. Create CSV or just use a spreadsheet

**You now have REAL leads to contact!**

#### Option C: Local Business Directories
- Yelp
- Yellow Pages
- Local Chamber of Commerce
- Walk around your neighborhood

---

### 4. Way to Contact Leads

**Current problem:** No way to actually SEND emails

**Solutions:**

#### Option A: Gmail (Recommended)
**Time:** 5 minutes
**Cost:** FREE

1. Create Gmail app password: https://myaccount.google.com/apppasswords
2. Add to `.env`:
   ```
   GMAIL_ADDRESS=your.email@gmail.com
   GMAIL_APP_PASSWORD=your_app_password
   ```
3. Test:
   ```bash
   python tools/send_emails.py leads/test.csv --dry-run
   ```

#### Option B: Manual Email (Works Now)
**Time:** 2 min per email
**Cost:** $0

1. Open Gmail/Outlook
2. Copy template from `templates/email_outreach.md`
3. Personalize: business name, city, etc.
4. Attach their PDF report
5. Send
6. Track in spreadsheet

**You can send 10 emails manually today!**

#### Option C: Walk-In (No Email Needed!)
**Time:** 30 min per business
**Cost:** Gas money

1. Generate their audit report PDF
2. Print it OR show on tablet
3. Walk in
4. Use pitch script from `sales-materials/pitch_scripts.md`

**This actually works better than email for first clients!**

---

## 🟡 IMPORTANT (Should have, but can work around)

### 5. Audit Reports Generated

**Status:** ❌ Only demo reports exist

**How to fix:**

```bash
# Generate 5 reports for your target businesses
python tools/bulk_audit.py --demo --count 5 \
  --your-name "Your Name" \
  --your-phone "(555) 123-4567"
```

**Better (with API):**
```bash
python tools/gbp_audit.py "Joe's Coffee" "Seattle, WA"
```

---

### 6. Landing Page Deployed

**Status:** ❌ Only HTML file, not live

**Why:** Capture leads 24/7 automatically

**How to fix (5 minutes):**

See `landing-page/README.md`

**Quick deploy to Netlify:**
1. Go to netlify.com
2. Drag `landing-page/` folder
3. Done - you get a URL

**OR skip for now** - Just use direct outreach first

---

## 🟢 NICE TO HAVE (Can add later)

### 7. Social Media Presence
- LinkedIn profile
- Facebook business page
- Instagram account

**Skip for Week 1** - Focus on direct sales

### 8. Paid Advertising
- Facebook Ads account
- Google Ads account
- $10-20/day budget

**Skip for Week 1** - Do manual outreach first

### 9. Email Automation
- GMass subscription
- Mailchimp account
- Lemlist account

**Skip for Week 1** - Send emails manually

---

## 🎯 MINIMUM VIABLE SETUP (Can Get Customer TODAY)

**You only NEED:**

1. ✅ Your contact info configured
2. ✅ One payment method (Venmo/Zelle/Cash)
3. ✅ 5-10 real business names from Google Maps
4. ✅ 5 audit reports generated (even demo mode is fine!)
5. ✅ Email templates copied and ready
6. ✅ Pitch script practiced

**That's it!**

**Don't need:**
- ❌ Google API (demo works for Week 1)
- ❌ Landing page (direct outreach works)
- ❌ Automated email sending (do manually)
- ❌ Social media (do later)
- ❌ Paid ads (do later)

---

## 📝 COMPLETE SETUP STEPS (30 minutes)

### Minute 0-10: Configure

```bash
# Run setup wizard
python setup_wizard.py

# This creates:
# - .env file with your info
# - MY_CONFIG.txt for reference
```

### Minute 10-15: Set Up Payment

- Download Venmo app
- OR check if Zelle is in your banking app
- Test sending $1 to yourself

### Minute 15-25: Find 10 Real Leads

**Manual method (no API needed):**
1. Open Google Maps
2. Search "coffee shop [your city]"
3. Find 10 with few photos
4. Write in spreadsheet:
   - Business name
   - Address
   - Phone
   - Industry (coffee shop)

### Minute 25-30: Generate Reports

```bash
# Generate 10 reports with YOUR info
python tools/bulk_audit.py --demo --count 10 \
  --your-name "Your Actual Name" \
  --your-phone "(Your Real Phone)" \
  --your-email "your@real-email.com"
```

**✅ YOU'RE NOW READY TO GET CUSTOMERS!**

---

## 🚀 HOW TO GET YOUR FIRST CUSTOMER TODAY

### Method 1: Walk-In (Recommended for First Client)

**Time:** 2-3 hours
**Success rate:** 10-30%
**Expected:** 1-2 clients if you visit 8-10 businesses

**Steps:**
1. Print 3-5 audit reports OR load on tablet
2. Drive to business district
3. Walk into businesses from your list
4. Use pitch: "Hi, is the owner available? I have something quick to show them about their Google listing."
5. Show their audit report (even if it's demo data, the gaps are usually real!)
6. Offer service: $179, can start today
7. If yes: Take deposit ($90), schedule service
8. If no: Leave contact info, move to next

**Visit 8 businesses = 1-2 clients = $179-358**

### Method 2: Email Outreach

**Time:** 1 hour
**Success rate:** 15-25% response, 5-10% close
**Expected:** 0-1 clients from 10 emails

**Steps:**
1. Find emails for your 10 leads (website, Google, call and ask)
2. Copy Email Template #1 from `templates/email_outreach.md`
3. Personalize each email (their business name, city, specific issues)
4. Attach their PDF audit report
5. Send from Gmail
6. Track in spreadsheet
7. Follow up in 3 days if no response

**Send 10 emails = 2-3 responses = 0-1 client**

### Method 3: Phone Calls

**Time:** 1 hour
**Success rate:** 20-40% to get owner, 10% close
**Expected:** 1 client from 10 calls

**Steps:**
1. Call businesses from your list
2. Ask for owner/manager
3. Use phone script from `sales-materials/pitch_scripts.md`
4. Offer to email audit report
5. Follow up next day
6. Book meeting if interested

---

## 🔧 TROUBLESHOOTING

### "I ran setup_wizard but PDFs still have placeholders"

**Fix:**
```bash
# Generate new reports with --your-name flags:
python tools/gbp_audit.py --demo \
  --your-name "Your Name" \
  --your-phone "(555) 123-4567" \
  --your-email "you@email.com"
```

### "Lead finder only gives fake businesses"

**You have 2 options:**
1. Get Google API (10 min setup, docs/API_SETUP_GUIDE.md)
2. Find real businesses manually on Google Maps (works fine!)

### "I don't have any emails for businesses"

**Solutions:**
1. Check their website's "Contact" page
2. Call and ask: "What's the best email to send this to?"
3. Use contact form on their website
4. Just do walk-ins instead - more effective anyway!

### "My Gmail won't send emails"

**Common fixes:**
1. Enable 2-factor authentication first
2. Create app password (not regular password)
3. Check .env file has correct GMAIL_ADDRESS and GMAIL_APP_PASSWORD
4. Or just send emails manually from Gmail for now

### "Nobody is responding to my emails"

**Try:**
1. Walk in instead - way higher success rate
2. Call first, then email
3. Improve personalization (mention specific things from their profile)
4. Send follow-ups (Day 3, Day 10)

### "I'm nervous to walk in / make calls"

**Tips:**
1. Start with 1-2 businesses you know (practice)
2. Remember: You're HELPING them (not selling)
3. Have audit report ready to show proof
4. Script it word-for-word first few times
5. Gets easier after #3!

---

## ✅ FINAL CHECKLIST

**Before attempting to get a customer:**

- [ ] Ran `python setup_wizard.py`
- [ ] Have payment method ready (Venmo/Zelle/Cash)
- [ ] Have list of 10 real businesses
- [ ] Generated 5-10 audit reports with MY info
- [ ] Practiced pitch script 3 times
- [ ] Decided on approach (walk-in/email/phone)
- [ ] Have follow-up system (spreadsheet to track)
- [ ] Know delivery process (docs/SERVICE_DELIVERY.md)

**If all checked ✅ → You're ready to go get a customer RIGHT NOW!**

---

## 🎯 REALISTIC EXPECTATIONS

### Week 1 (Manual Mode):
- Time: 10-15 hours
- Leads contacted: 20-30
- Responses: 5-8
- Clients: 1-3
- Revenue: $179-537

### Week 2 (Getting Better):
- Time: 10-15 hours
- Leads contacted: 30-50
- Responses: 10-15
- Clients: 3-5
- Revenue: $537-895

### Week 3+ (System Working):
- Time: 10 hours
- Leads: 50+ (partially automated)
- Clients: 5-10
- Revenue: $895-1,790

---

## 💡 BOTTOM LINE

**You DON'T need:**
- Google API (nice to have, not required)
- Landing page deployed (can add later)
- Email automation (send manually first)
- Paid ads (do organic first)
- Perfect setup (good enough beats perfect)

**You DO need:**
- Your real contact info configured
- Payment method ready
- 5-10 business names to contact
- Reports generated
- Willingness to reach out

**The system works with demo mode for Week 1!**

The audit reports point out real problems (low photos, no posts) even with fake data. Most businesses actually DO have these issues.

**Stop setting up. Start selling.**

Run setup_wizard, find 10 businesses, make contact, get paid.

Everything else can wait.

**Go! 🚀**
