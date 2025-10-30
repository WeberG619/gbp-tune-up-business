# Setup Guide

Get your system ready to start landing clients in 2 hours.

---

## ⚡ QUICK START (15 minutes)

### 1. Clone the Repository

```bash
git clone https://github.com/WeberG619/gbp-tune-up-business.git
cd gbp-tune-up-business
```

### 2. Install Python Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Test the Audit Tool (Demo Mode)

```bash
# Run without API key (uses demo data)
python tools/gbp_audit.py --demo

# Should output a sample audit report
```

✅ **If you see an audit report, you're good to go!**

---

## 🔑 GOOGLE API SETUP (Optional - 30 minutes)

The audit tool works in **demo mode** without API keys, but for real data, you'll need Google Places API access.

### Step 1: Create Google Cloud Account

1. Go to https://console.cloud.google.com/
2. Sign in with your Google account
3. Click "Select a project" → "New Project"
4. Name it: "GBP-Business-Tool"
5. Click "Create"

### Step 2: Enable APIs

1. Go to **APIs & Services** → **Library**
2. Search for and enable these APIs:
   - **Places API**
   - **Maps JavaScript API** (optional, for enhanced features)

### Step 3: Create API Credentials

1. Go to **APIs & Services** → **Credentials**
2. Click **Create Credentials** → **API Key**
3. Copy your API key

### Step 4: Configure Environment

```bash
# Copy example env file
cp .env.example .env

# Edit .env and add your API key
# GOOGLE_PLACES_API_KEY=your_actual_api_key_here
```

### Step 5: Test with Real Data

```bash
python tools/gbp_audit.py "Starbucks" "Seattle, WA"

# Should pull real data from Google Places API
```

### API Costs (Free Tier)

- **Free:** First $200/month in usage
- **Cost per request:** ~$0.017 per place details request
- **Monthly budget:** ~11,000 requests free
- **Your usage:** ~30 requests/day = $0.51/day = **~$15/month**

**Result:** Likely free for first 2-3 months while you're getting started.

---

## 📸 PHOTO EDITING SETUP (15 minutes)

### Option 1: Lightroom Mobile (Recommended - FREE)

**iOS/Android:**
1. Download **Adobe Lightroom** (free version)
2. Import photos
3. Use presets or manual editing
4. Export optimized JPEGs

**Desktop:**
1. Download **GIMP** (free Photoshop alternative)
   - https://www.gimp.org/downloads/
2. Or use **Photopea** (free, browser-based)
   - https://www.photopea.com/

### Option 2: Automated with Python

```bash
# Install additional image processing library
pip install opencv-python

# Use the batch processor
python tools/photo_processor.py input_folder/ output_folder/
```

### Create Presets

**Save this as your "GBP Enhancement" preset in Lightroom:**

- Exposure: +15
- Contrast: +10
- Highlights: -10
- Shadows: +15
- Whites: +10
- Blacks: -5
- Clarity: +15
- Vibrance: +10
- Saturation: +5
- Sharpening: +40

**Apply to all photos in one tap.**

---

## 💳 PAYMENT PROCESSING SETUP (10 minutes)

### Option 1: Venmo (Easiest - FREE)

1. Download Venmo app
2. Link bank account
3. Share your @username with clients
4. **Fees:** Free for personal payments

**Pros:** Instant, everyone has it
**Cons:** Looks less professional

---

### Option 2: Square (Best for Business)

1. Sign up at https://squareup.com/
2. Download Square Point of Sale app
3. Get free card reader (optional)
4. **Fees:** 2.6% + $0.10 per transaction

**Pros:** Professional, supports all payment types
**Cons:** Small fee per transaction

---

### Option 3: Cash

- No fees
- Immediate payment
- No chargebacks

**Downside:** Inconvenient, requires cash handling

---

**Recommendation:** Start with Venmo/Cash, upgrade to Square after 10 clients.

---

## 🗂️ CLIENT MANAGEMENT (15 minutes)

### Option 1: Google Sheets (FREE)

**Create a spreadsheet with these columns:**

| Date | Client | Contact | Status | Paid | Delivered | Next Action |
|------|--------|---------|--------|------|-----------|-------------|

**Statuses:**
- Lead
- Pitched
- Closed
- Delivered
- Monthly (recurring)

**Template:**
Copy this: https://docs.google.com/spreadsheets/d/[YOUR_TEMPLATE_ID]

---

### Option 2: Airtable (FREE tier)

1. Sign up at https://airtable.com/
2. Create a base from template: "CRM"
3. Customize fields:
   - Client name
   - Contact info
   - Service type
   - Status
   - Payment amount
   - Delivery date

**Pros:** More powerful, includes automation
**Cons:** Slight learning curve

---

### Option 3: Notion (FREE)

1. Sign up at https://notion.so/
2. Create database for clients
3. Add kanban board view (Lead → Pitched → Closed → Delivered)

**Pros:** Very flexible, great for solo operators
**Cons:** Can be overwhelming

---

**Recommendation:** Start with Google Sheets, upgrade to Airtable after 20 clients.

---

## 📱 MOBILE SETUP (10 minutes)

### Essential Apps

**Photo/Camera:**
- iOS: Default Camera app (use Portrait mode)
- Android: Google Camera or Open Camera

**Photo Editing:**
- Lightroom Mobile (FREE)
- Snapseed (FREE - Google's editor)

**Google Business Profile Management:**
- Google Business Profile app (iOS/Android)
- Google Maps (to preview how customers see it)

**Communication:**
- Gmail (for client emails)
- Your preferred text app (SMS)

**Payment:**
- Venmo / Cash App / Square

**File Storage:**
- Google Drive (store client photos)
- Dropbox (alternative)

---

## 🖥️ DESKTOP TOOLS (Optional)

### Batch Photo Editing

**Windows/Mac/Linux:**
- **GIMP** (free Photoshop alternative)
- **Darktable** (free Lightroom alternative)
- **XnConvert** (batch conversion/resize)

### PDF Generation (for reports)

Already included in requirements.txt:
```bash
pip install reportlab
```

### Automation

**Zapier / Make.com:**
- Auto-post to Google Business Profile
- Auto-send follow-up emails
- Sync client data

**Cost:** Free tier available

---

## 📚 TEMPLATE SETUP (5 minutes)

### Load Templates on Your Phone

**Create a Google Doc with:**

1. **Posts Templates**
   - Copy from `templates/post_templates.md`
   - Save as "GBP Post Templates"

2. **Q&A Templates**
   - Copy from `templates/qa_templates.md`
   - Save as "GBP Q&A Templates"

3. **Review Replies**
   - Copy from `templates/review_replies.md`
   - Save as "GBP Review Replies"

**Access from your phone while on-site with clients.**

---

### Create Keyboard Shortcuts (iOS)

**Settings → General → Keyboard → Text Replacement**

Add these:

| Shortcut | Phrase |
|----------|--------|
| `gbpthank` | "Thank you for the 5-star review, [NAME]! We're thrilled you had a great experience. Looking forward to serving you again soon!" |
| `gbppitch` | "Hi [NAME], I noticed your Google Business profile is missing [X] photos and [Y] posts. I can upgrade it in 90 minutes for $179. Interested?" |
| `gbpfollowup` | "Hi [NAME]! It's been 2 weeks since we upgraded your Google profile. Seeing any more calls or traffic? Would love a quick review if you're happy with the results!" |

---

## 🎯 BUSINESS SETUP (30 minutes)

### 1. Create Your Own Google Business Profile

**Yes, YOU need one too.**

1. Go to https://business.google.com/
2. Add your business:
   - Name: "[Your Name] - Google Business Profile Optimization" or "[City] GBP Services"
   - Category: "Marketing Consultant" or "Internet Marketing Service"
   - Service area: [Your city/region]

3. Verify your business
4. Add your services:
   - Google Business Profile Setup - $179
   - Monthly Profile Management - $59/mo
   - Photo Enhancement - $99

5. Upload a professional photo of yourself
6. Create your first 3 posts

**Why:** Clients will Google you. You need to look legit.

---

### 2. Set Up Review Collection

**Your review link:**
`https://g.page/[your-business]/review`

**Use this to ask clients for reviews after delivery.**

---

### 3. Create Business Cards (Optional)

**Vistaprint / Moo / Canva:**

**Front:**
```
[YOUR NAME]
Google Business Profile Expert

Get More Customers Through Google
$179 Setup | $59/mo Maintenance

[PHONE] | [EMAIL]
```

**Back:**
```
✓ Professional Photos
✓ Weekly Posts
✓ Profile Optimization
✓ Review Management

[YOUR WEBSITE or Social]
```

**Cost:** $20-50 for 250 cards

**Alternative:** Just save your contact card and AirDrop/text it.

---

### 4. Simple Website (Optional - 30 min)

**Use Carrd.co (FREE):**

1. Sign up at https://carrd.co/
2. Choose "Landing Page" template
3. Customize with:
   - Headline: "Get More Customers Through Google"
   - Subhead: "Professional Google Business Profile Optimization for [City] Businesses"
   - Services list
   - Pricing
   - Contact form
   - Before/after examples (once you have them)

**Result:** [yourname].carrd.co

**Cost:** Free (or $19/year for custom domain)

---

## ✅ FINAL SETUP CHECKLIST

### Tools Ready
- [ ] Python tools installed and tested
- [ ] Photo editing app installed on phone
- [ ] Payment method set up (Venmo/Square)
- [ ] Client tracking spreadsheet created
- [ ] Templates loaded on phone

### Your Business
- [ ] Your own Google Business Profile created
- [ ] Your review link saved
- [ ] Business cards ordered (or digital contact ready)
- [ ] Simple website launched (optional)

### Knowledge
- [ ] Read `CUSTOMER_ACQUISITION.md`
- [ ] Read `SERVICE_DELIVERY.md`
- [ ] Practiced pitch script 5+ times
- [ ] Watched 2-3 YouTube videos on GBP optimization

### First Client Prep
- [ ] Built audit reports for 10 local businesses
- [ ] Planned tomorrow's route (8-10 businesses)
- [ ] Phone/tablet charged
- [ ] Confidence level: 8/10+

---

## 🚀 YOU'RE READY!

**Next steps:**

1. **Tonight:** Build 10 audit reports for businesses you'll visit tomorrow
2. **Tomorrow morning:** Review pitch script one more time
3. **Tomorrow 9am:** Walk into your first business
4. **Tomorrow 5pm:** Celebrate your first client!

---

## 🆘 TROUBLESHOOTING

### Issue: Python not installed

**Mac:**
```bash
brew install python3
```

**Windows:**
Download from https://www.python.org/downloads/

**Linux:**
```bash
sudo apt-get install python3 python3-pip
```

---

### Issue: pip install fails

**Try:**
```bash
pip install --upgrade pip
pip install -r requirements.txt --user
```

---

### Issue: Google API quota exceeded

**Solution:**
- Use demo mode: `python tools/gbp_audit.py --demo`
- Wait 24 hours for quota to reset
- Or upgrade Google Cloud plan

---

### Issue: Can't access Google Business Profile

**Check:**
1. Business is verified
2. You're added as a manager
3. Using the correct Google account

**Fix:**
Ask client to add you:
- Google Business Profile → Settings → Users → Add user → [YOUR EMAIL] → Manager

---

## 💡 PRO TIPS

1. **Test everything on YOUR OWN business first** - Great practice, plus you'll have before/after examples

2. **Bookmark this checklist** - Reference it before each client

3. **Keep tools simple** - Don't over-complicate with too many apps

4. **Mobile-first** - Most of your work will be done on your phone on-site

5. **Back up client photos** - Always save to Google Drive (clients ask for them later)

---

**You're all set! Time to make money. 💰**
