# Google API Setup Guide

**When to do this:** After you've practiced with demo mode and are ready to generate real audit reports for actual businesses.

**Cost:** FREE for up to 28,000 requests per month (more than enough for this business)

**Time required:** 10-15 minutes

---

## Why You Need the API

The Google Places API allows your audit tool to:
- Pull real data about any business's Google Business Profile
- Get accurate photo counts, review numbers, and ratings
- Find and analyze competitors automatically
- Generate professional audit reports with real data

**Without API:** Demo mode works great for practice and examples, but uses random data.
**With API:** Get real, accurate data for actual client businesses.

---

## Step-by-Step Setup

### Step 1: Create a Google Cloud Account

1. Go to: **https://console.cloud.google.com/**

2. Sign in with any Google/Gmail account
   - Use your personal Gmail
   - OR create a new Gmail specifically for business

3. Accept the Terms of Service

### Step 2: Create a New Project

1. Click the **project dropdown** at the top of the page
   - It says "Select a project" or shows current project name

2. Click **"NEW PROJECT"**

3. Fill in project details:
   - **Project name:** `GBP-Business` (or whatever you want)
   - **Organization:** Leave as "No organization"
   - Click **"CREATE"**

4. Wait 10-15 seconds for project creation

5. Select your new project from the dropdown

### Step 3: Enable the Places API

1. In the search bar at the top, type: `Places API`

2. Click on **"Places API"** in the results

3. Click the blue **"ENABLE"** button

4. Wait 30 seconds for it to enable

You'll see "API enabled" confirmation

### Step 4: Create API Credentials

1. Click **"Credentials"** in the left sidebar menu

2. Click **"+ CREATE CREDENTIALS"** at the top

3. Select **"API key"**

4. Your API key will appear in a popup window
   - It looks like: `AIzaSyD1234567890abcdefghijklmnopqrstuvwx`
   - **COPY IT IMMEDIATELY** - you'll need this

5. Keep this window open (we'll restrict the key next)

### Step 5: Restrict Your API Key (IMPORTANT!)

This prevents abuse and protects you from unexpected charges.

1. In the popup, click **"EDIT API KEY"** (or close popup and click pencil icon next to your key)

2. **Give it a name:**
   - Name: `GBP Audit Tool Key`

3. **Set API restrictions:**
   - Find "API restrictions" section
   - Select **"Restrict key"**
   - Click **"Select APIs"** dropdown
   - Check ONLY: **"Places API"**
   - Uncheck everything else

4. **Application restrictions (optional but recommended):**
   - Select "IP addresses"
   - Click "ADD AN ITEM"
   - Add your computer's IP (or leave blank for now)

5. Click **"SAVE"**

### Step 6: Enable Billing (Required but FREE)

Google requires a credit card on file, but **won't charge you** unless you exceed free limits.

**FREE Tier:**
- **28,000 requests per month** = FREE
- That's about 900 requests per day
- You'll use maybe 50-200 per month maximum

**If you exceed free tier:**
- Additional requests cost $0.017 each (about 2 cents)
- You'd need to do 1,600+ audits per month to pay anything

**To set up billing:**

1. Click **"Billing"** in the left menu

2. Click **"LINK A BILLING ACCOUNT"**

3. Click **"CREATE BILLING ACCOUNT"**

4. Fill in your information:
   - Country
   - Account type: **Individual** (unless you have a registered business)
   - Name and address
   - Credit card information

5. Click **"START MY FREE TRIAL"** or **"SUBMIT AND ENABLE BILLING"**

6. Accept terms

**Note:** Google gives new accounts $300 in free credits that last 90 days, so you definitely won't be charged for a while!

---

## Step 7: Add API Key to Your Project

Now that you have your API key, let's add it to your project.

### Option A: Using .env File (Recommended)

1. In your project folder, find the file `.env.example`

2. Copy it and rename to `.env`:
   ```bash
   cp .env.example .env
   ```

3. Open `.env` in a text editor

4. Replace `your_api_key_here` with your actual API key:
   ```
   GOOGLE_PLACES_API_KEY=AIzaSyD1234567890abcdefghijklmnopqrstuvwx
   ```

5. Save the file

**IMPORTANT:** Never share this file or commit it to GitHub! It's already in `.gitignore`.

### Option B: Using Command Line Flag

You can also pass the API key directly when running the tool:

```bash
python tools/gbp_audit.py "Business Name" "City, State" --api-key "YOUR_API_KEY_HERE"
```

---

## Step 8: Test Your API Key

Let's make sure it works!

```bash
# Test with a real business
python tools/gbp_audit.py "Starbucks" "Seattle, WA"
```

**If it works, you'll see:**
- Real data (not "demo mode" message)
- Actual photo counts, reviews, ratings
- PDF report generated with real information

**If you see errors:**
- "403 Forbidden" = API key not set up correctly
  - Double-check you enabled Places API
  - Make sure API key is correctly copied
- "Invalid API key" = Check for typos in your key
- "Billing not enabled" = Complete Step 6

---

## Monitoring Your Usage

### Check How Many Requests You're Using

1. Go to: https://console.cloud.google.com/

2. Select your project

3. Click **"APIs & Services" → "Dashboard"**

4. You'll see a graph of your API usage

**Typical usage for this business:**
- 10 clients/week = ~40 requests/month
- Well under the 28,000 free limit!

### Set Up Usage Alerts (Optional)

1. Go to **Billing → Budgets & alerts**

2. Click **"CREATE BUDGET"**

3. Set budget to $5 (more than enough buffer)

4. Enable email alerts at 50%, 90%, 100%

This way you'll know if something goes wrong!

---

## Troubleshooting

### "API key not valid"
- Make sure you copied the entire key (usually starts with `AIza`)
- No extra spaces before or after
- Check `.env` file format is correct

### "This API project is not authorized"
- Go back to Step 3 and make sure Places API is enabled
- Wait 5 minutes and try again (sometimes takes time to propagate)

### "You have exceeded your daily request quota"
- Very unlikely with 28,000 free requests
- Check usage in console
- Make sure API key isn't being used elsewhere

### "REQUEST_DENIED"
- Billing not enabled (see Step 6)
- API key restrictions too strict
- Try creating a new unrestricted key for testing

---

## Security Best Practices

### DO:
✓ Keep your API key private
✓ Use .env file (not hard-coded in scripts)
✓ Add .env to .gitignore
✓ Restrict API key to only Places API
✓ Monitor your usage monthly

### DON'T:
✗ Share your API key publicly
✗ Commit API key to GitHub
✗ Use it in client-side JavaScript (websites)
✗ Give it to others
✗ Leave it unrestricted

### If Your Key is Compromised:

1. Go to Google Cloud Console
2. Click "Credentials"
3. Find your key and click trash icon to delete it
4. Create a new key (repeat Steps 4-5)

---

## Cost Breakdown

**Your Expected Monthly Usage:**

| Activity | Requests | Cost (after free tier) |
|----------|----------|------------------------|
| 5 audits/week | ~80/month | $0.00 (under free tier) |
| 20 audits/week | ~320/month | $0.00 (under free tier) |
| 100 audits/week | ~1,600/month | $0.00 (under free tier) |
| 700 audits/week | ~28,000/month | $0.00 (exactly at free tier) |

**You'd need to audit 700 businesses per week to start paying anything!**

For this business, expect:
- **Month 1:** 10-20 audits = $0.00
- **Month 2:** 30-50 audits = $0.00
- **Month 3:** 50-100 audits = $0.00

**Total annual cost estimate: $0.00** (unless you scale to 50+ clients/week)

---

## Alternative: Skip API for Now

**You can run this entire business in demo mode!**

Here's how:

1. **Use demo mode for examples and practice:**
   ```bash
   python tools/gbp_audit.py --demo
   ```

2. **For real client audits:**
   - Visit their Google Business Profile manually
   - Count photos, reviews, etc.
   - Edit the demo report PDF in Canva or Photoshop with real numbers
   - OR use demo reports as conversation starters, then do manual audit

3. **When you have 5-10 paying clients:**
   - Set up API to save time
   - Automate the audit process
   - Scale faster

**Bottom line:** API is helpful but not required to start making money!

---

## Next Steps

Once your API is set up:

1. **Generate real audit reports:**
   ```bash
   python tools/gbp_audit.py "Local Business" "Your City, State"
   ```

2. **Create your portfolio:**
   - Generate 5-10 real audits for businesses in your area
   - Use these as examples when pitching
   - Show the gap between their score and competitors

3. **Start selling:**
   - Walk into businesses with their real audit in hand
   - Much more compelling than demo data!

4. **Optional: Automate further:**
   - Build a simple web form to collect business names
   - Generate audits in bulk
   - Email reports automatically

---

## Questions?

**Google Cloud Help:** https://cloud.google.com/docs/get-started

**Places API Docs:** https://developers.google.com/maps/documentation/places/web-service

**Billing Help:** https://cloud.google.com/billing/docs

**Project Issues:** Open an issue on GitHub

---

**You're all set! Start generating real audit reports and close more deals! 🚀**
