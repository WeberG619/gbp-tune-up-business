# 🔑 How to Get REAL Business Data

## 🎭 Demo Mode vs. Real Mode

### What You're Seeing Now (Demo Mode)
- ❌ Fake business names ("Morning Grind Cafe")
- ❌ Fake phone numbers ((555) 123-4567)
- ❌ Fake addresses (123 Main St)
- ❌ Can't actually contact these businesses

### What You'll Get (Real Mode)
- ✅ Real business names from Google Maps
- ✅ Real phone numbers you can call
- ✅ Real addresses you can visit
- ✅ Real review counts and ratings
- ✅ Real photo counts from their Google profiles

---

## 🚀 Quick Setup (10 Minutes)

### Step 1: Get Google Places API Key

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/
   - Sign in with your Google account

2. **Create a Project**
   - Click "Select a project" (top left)
   - Click "New Project"
   - Name: "GBP Business"
   - Click "Create"

3. **Enable Places API**
   - Use search bar: type "Places API"
   - Click on "Places API"
   - Click "Enable" button

4. **Create API Key**
   - Left sidebar: Click "Credentials"
   - Click "Create Credentials" → "API Key"
   - Copy your API key (starts with `AIzaSy...`)

5. **Enable Billing (Required but FREE)**
   - Click "Billing" in left sidebar
   - Link a credit card (for verification only)
   - **First $200/month is FREE**
   - That's 40,000 searches/month
   - You'll use ~200 searches total
   - **Cost: $0**

---

### Step 2: Add API Key to Project

Run this interactive setup:

```bash
python3 setup_api.py
```

It will ask you for:
- Your Google API key
- Your name
- Your phone
- Your email

**Or create `.env` file manually:**

```bash
# Create .env file
nano .env
```

Add this:
```
GOOGLE_PLACES_API_KEY=AIzaSyB...your-key-here...
YOUR_NAME=Your Name
YOUR_PHONE=(208) 555-1234
YOUR_EMAIL=your.email@gmail.com
```

Save and exit (Ctrl+X, Y, Enter)

---

### Step 3: Run with Real Data

```bash
# This will get REAL businesses
python3 tools/market_mapper.py \
  --locations "Sandpoint, ID" "Coeur d'Alene, ID" "Spokane, WA" \
  --industries "coffee shop" "salon" "gym" "restaurant" \
  --limit 20
```

**No more `--demo` flag!**

---

## 💰 Cost Breakdown

### Google Places API Pricing

**Free Tier:**
- $200/month credit
- = 40,000 Place Details requests
- = 200,000 Place Search requests

**What You'll Use:**
- 180 businesses × 2 requests each = **360 requests**
- **Cost: $0** (well within free tier)

**Even if you search 100 cities:**
- 18,000 businesses × 2 = 36,000 requests
- **Still FREE** (under 40,000 limit)

### Important:
- Google requires a credit card for verification
- But you won't be charged unless you exceed $200/month
- That would require 40,000+ searches
- You're doing ~200 searches
- **You will NOT be charged**

---

## 🎯 What Changes with Real Data?

### Demo Mode (Current)
```
Morning Grind Cafe
Phone: (555) 966-3443
Address: 3581 Main St, Sandpoint, ID
Rating: 3.6
Reviews: 28
Photos: 4
```
❌ Can't call this number (fake)
❌ Can't visit this address (fake)
❌ Can't verify these details

### Real Mode (After API Setup)
```
Evans Brothers Coffee
Phone: (208) 263-5417
Address: 314 N 1st Ave, Sandpoint, ID 83864
Rating: 4.7
Reviews: 142
Photos: 78
```
✅ Real phone number - call them now!
✅ Real address - visit them today!
✅ Real data from their actual Google Business Profile

---

## 🔧 Testing Your API Key

After setup, test it:

```bash
# Test with just 1 business
python3 tools/market_mapper.py \
  --locations "Sandpoint, ID" \
  --industries "coffee shop" \
  --limit 1
```

**You should see:**
```
🔍 Searching: coffee shop in Sandpoint, ID
✅ Using Google Places API
📡 Fetching real business data...

🔥 [Real Business Name]
   Score: 85 | Priority: HIGH
   [Real phone number]
   [Real address]
```

---

## 🐛 Troubleshooting

### "API key not valid"
- Check you copied the entire key
- Make sure Places API is enabled
- Wait 2-3 minutes after creating key (propagation)

### "Billing not enabled"
- Go to Google Cloud Console → Billing
- Link a credit card
- You won't be charged (free tier)

### "Permission denied"
- Make sure you enabled "Places API" (not just "Maps API")
- Check API key restrictions

### "Still showing demo data"
- Remove `--demo` flag from command
- Make sure `.env` file exists and has API key
- Run: `cat .env` to verify

---

## 📊 What You Get with Real Data

### Current (Demo):
- 180 fake businesses
- Can't contact anyone
- Just for testing the system

### After API Setup:
- 180+ REAL businesses
- Real phone numbers to call
- Real addresses to visit
- Accurate scores based on actual Google profiles
- Can start making money TODAY

---

## ⚡ Quick Commands

### Check if API key is set:
```bash
cat .env | grep GOOGLE_PLACES_API_KEY
```

### Run with real data:
```bash
python3 tools/market_mapper.py \
  --locations "Sandpoint, ID" \
  --industries "coffee shop" \
  --limit 10
```

### Test single search:
```bash
python3 tools/market_mapper.py \
  --locations "Sandpoint, ID" \
  --industries "coffee shop" \
  --limit 1
```

---

## 🎯 Summary

**To get REAL businesses:**

1. **Get Google API key** (10 min, FREE)
   → https://console.cloud.google.com/

2. **Run setup:**
   ```bash
   python3 setup_api.py
   ```

3. **Generate real leads:**
   ```bash
   python3 tools/market_mapper.py \
     --locations "Sandpoint, ID" \
     --industries "coffee shop" \
     --limit 20
   ```

4. **Start calling real businesses!**

---

## 💡 Why Demo Mode Exists

Demo mode is for:
- ✅ Testing the system without API key
- ✅ Learning how the tools work
- ✅ Seeing what the output looks like
- ✅ Making sure everything is installed correctly

But to actually make money, you need **real businesses with real contact info** = need Google API key.

---

## 🚀 Ready to Get Started?

Run this now:

```bash
python3 setup_api.py
```

Follow the prompts, paste your API key, and you'll be searching real businesses in 2 minutes!

**Or read the full API guide:**
```bash
cat docs/API_SETUP_GUIDE.md
```
