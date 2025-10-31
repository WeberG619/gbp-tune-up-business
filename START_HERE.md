# 🚀 START HERE - Run Your Automation

## ⚡ FASTEST WAY (One Command)

### Option 1: Run with Python
```bash
python3 RUN_ME.py
```

### Option 2: Run with Bash
```bash
./run_everything.sh
```

### Option 3: Interactive Menu
```bash
./automate.sh
```
Then choose option 5.

**All three do the same thing!** Choose whichever is easiest for you.

---

## 📋 What Happens When You Run It

1. **Generates 180 leads** (takes 1-2 minutes)
   - Searches Sandpoint, Coeur d'Alene, Spokane
   - Scores each business 0-100
   - Finds businesses with poor Google profiles

2. **Creates your interactive map**
   - Opens in your web browser automatically
   - Shows all 180 businesses as pins
   - Click pins to see phone numbers

3. **Shows your top 10 targets**
   - Businesses with highest scores
   - Phone numbers
   - Pitch scripts

4. **Creates files:**
   - `maps/complete_map.html` - Interactive map
   - `maps/market_leads_*.csv` - Spreadsheet with all businesses
   - `maps/action_plan_*.md` - Your action plan

---

## 🎯 After Running Automation

### Step 1: Look at the Map
The map should open automatically in your browser.

**If it doesn't open:**
```bash
# Mac:
open maps/complete_map.html

# Linux:
xdg-open maps/complete_map.html

# Or just double-click the file
```

### Step 2: Read Your Action Plan
```bash
cat maps/action_plan_*.md
```

This shows your top 10 targets with phone numbers.

### Step 3: Contact Businesses

**Option A: Call them**
```bash
# Use phone numbers from the action plan or map
# Script: "Hi, I noticed [BUSINESS] only has X photos on Google.
#          This is costing you customers. Can I show you a free audit?"
```

**Option B: Email them**
```bash
# Prepare 10 emails (doesn't send, just prepares)
python3 tools/auto_email_sender.py send --batch 10

# Actually send them
python3 tools/auto_email_sender.py send --batch 10 --send
```

**Option C: Visit them**
```bash
# Look at map, filter to your city, visit 5-10 businesses
# Walk-ins have 30-40% close rate (highest!)
```

---

## 💻 All Commands Reference

### Generate Leads Only
```bash
python3 tools/market_mapper.py --demo --limit 15
```

### View Map
```bash
open maps/complete_map.html
```

### Send Emails (Dry Run)
```bash
python3 tools/auto_email_sender.py send --batch 10
```

### Send Emails (Actually Send)
```bash
python3 tools/auto_email_sender.py send --batch 10 --send
```

### Check Follow-ups
```bash
python3 tools/auto_email_sender.py followup
```

### View Analytics
```bash
open automation_data/dashboard.html
```

### Run Complete Automation
```bash
python3 tools/automation_master.py --auto-run
```

---

## 🐛 Troubleshooting

### "Python not found"
```bash
# Try python instead of python3
python RUN_ME.py
```

### "Permission denied"
```bash
# Make scripts executable
chmod +x RUN_ME.py
chmod +x run_everything.sh
chmod +x automate.sh
```

### "Map won't open"
```bash
# Find the map file
ls maps/

# Open manually
open maps/complete_map.html
# Or double-click it in your file browser
```

### "No leads generated"
```bash
# Run the market mapper directly
python3 tools/market_mapper.py --demo --limit 15

# Check output
ls maps/
```

---

## 📞 Quick Reference

### I want to...

**See all businesses on a map**
→ `open maps/complete_map.html`

**Get phone numbers to call**
→ `cat maps/action_plan_*.md` or click pins on map

**Send emails automatically**
→ `python3 tools/auto_email_sender.py send --batch 10 --send`

**Check who to follow up with**
→ `python3 tools/auto_email_sender.py followup`

**See my progress/analytics**
→ `open automation_data/dashboard.html`

**Start over / run everything again**
→ `python3 RUN_ME.py`

---

## ⏱️ Time Investment

- **First time setup**: 5 minutes (run automation)
- **Daily**: 30 minutes (check follow-ups, make calls)
- **Weekly**: 1 hour (send email batches)
- **Per client**: 90 minutes (service delivery)

**Expected: 2-3 clients/week = $358-537/week**

---

## 🎉 You're Ready!

Run this now:
```bash
python3 RUN_ME.py
```

Then start calling the businesses from your action plan!

**Good luck!** 💰
