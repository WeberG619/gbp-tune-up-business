# Customer Acquisition Automation Guide

**How to find 50+ leads per day and automate your outreach completely.**

This guide shows you how to use the automated tools to find customers online instead of door-to-door sales.

---

## 🎯 AUTOMATION STRATEGY OVERVIEW

**The System:**
1. **Find leads** → Automated lead finder tool
2. **Generate reports** → Bulk audit generator
3. **Send emails** → Email templates + mail merge
4. **Capture inbound** → Landing page running 24/7
5. **Social media** → Pre-written posts
6. **Paid ads** → Template campaigns

**Result:** 20-50 qualified leads per week with minimal manual work

---

## 🚀 QUICK START: Your First 50 Leads (This Week)

### Day 1: Find 50 Leads (1 hour)

```bash
# Find coffee shops in your city
python tools/lead_finder.py "Your City, ST" --industry "coffee shop" --limit 50

# Find salons
python tools/lead_finder.py "Your City, ST" --industry "salon" --limit 50

# Find gyms
python tools/lead_finder.py "Your City, ST" --industry "gym" --limit 50
```

**Output:** 3 CSV files in `leads/` folder with 150 total leads

**What it does:**
- Searches Google for businesses matching your criteria
- Analyzes their Google Business Profiles
- Scores them (higher score = better opportunity)
- Saves qualified leads to CSV

**Without API:**
- Uses realistic demo data
- Perfect for practice
- Can still use for real outreach (just verify business exists first)

**With API:**
- Gets real business data
- Accurate analysis
- Ready to use immediately

### Day 2: Generate Audit Reports (2 hours)

```bash
# Generate reports for top 20 leads from your coffee shop CSV
python tools/bulk_audit.py leads/leads_TIMESTAMP.csv \
  --your-name "Your Name" \
  --your-phone "(555) 123-4567" \
  --your-email "you@email.com"
```

**Output:** 20 professional PDF audit reports in `reports/bulk_TIMESTAMP/`

**What it does:**
- Reads your leads CSV
- Generates a custom audit report for each business
- Saves PDFs with professional branding
- Ready to attach to emails

**Time per report:** ~2 seconds
**Total time:** 40 seconds for 20 reports

### Day 3: Send Outreach Emails (2 hours)

**Manual approach (Week 1):**
1. Open leads CSV
2. For each lead:
   - Copy email template from `templates/email_outreach.md`
   - Personalize with their business name, city
   - Attach their specific audit report PDF
   - Send
3. Track in client tracking spreadsheet

**Send:** 10-20 emails per day

**Semi-automated approach (Week 2+):**
Use mail merge tool like:
- GMass (Gmail add-on)
- Mailchimp
- Lemlist
- Reply.io

**Configuration:**
1. Upload leads CSV
2. Map fields (business_name → {business_name})
3. Attach corresponding PDFs
4. Schedule sends

**Send:** 50-100 emails per day

### Day 4-7: Follow Up & Track

- Day 4: Respond to replies
- Day 6: Send Follow-up #1 to non-responders (Email Template #2)
- Day 13: Send Follow-up #2 to non-responders (Email Template #3)

**Track everything in `templates/client_tracking_template.csv`**

---

## 📊 COMPLETE AUTOMATION WORKFLOW

### The Full System (Once You're Profitable)

```
┌─────────────────┐
│  Lead Finder    │  ← Runs daily, finds 20 new leads
│  (Automated)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Lead Scoring   │  ← Auto-scores, filters low quality
│  (Automated)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Bulk Audit     │  ← Generates reports automatically
│  (Automated)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Email Sequence │  ← Sends personalized emails + follows up
│  (Automated)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Landing Page   │  ← Inbound leads fill form
│  (24/7 passive) │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  CRM/Tracker    │  ← You follow up and close
│  (You handle)   │
└─────────────────┘
```

**Time investment after setup:** 1-2 hours per day
**Lead flow:** 20-50 new leads per week
**Close rate:** 5-10% = 1-5 new clients per week
**Revenue:** $179-895 per week on autopilot

---

## 🔧 TOOL-BY-TOOL GUIDE

### 1. Lead Finder (`tools/lead_finder.py`)

**Purpose:** Find businesses with poor Google Business Profiles

**Basic usage:**
```bash
python tools/lead_finder.py "Austin, TX" --industry "salon"
```

**Advanced options:**
```bash
python tools/lead_finder.py "Austin, TX" \
  --industry "hair salon" \
  --limit 50 \
  --min-score 60 \
  --output leads/austin_salons.csv
```

**Parameters:**
- `location`: City, State
- `--industry`: Business type (coffee shop, salon, gym, etc.)
- `--limit`: Number of businesses to search (default: 20)
- `--min-score`: Minimum quality score (default: 40)
- `--output`: Custom output file path
- `--demo`: Use demo mode (no API required)

**Output CSV columns:**
- priority: HIGH/MEDIUM/LOW
- score: 0-100 (higher = better lead)
- business_name
- phone
- address
- rating
- reviews
- photos
- website
- reasons: Why they're a good lead
- place_id: For Google API reference

**Pro tips:**
- Target score 60+ for best conversion
- Run multiple industries per day
- Review CSV and prioritize HIGH priority leads first
- Verify phone numbers before calling

### 2. Bulk Audit Generator (`tools/bulk_audit.py`)

**Purpose:** Create professional PDF reports for many businesses at once

**Basic usage:**
```bash
python tools/bulk_audit.py leads/leads_20251031.csv \
  --your-name "John Smith" \
  --your-phone "(555) 123-4567" \
  --your-email "john@example.com"
```

**Demo mode (practice):**
```bash
python tools/bulk_audit.py --demo --count 10
```

**Parameters:**
- CSV file path (from lead_finder.py)
- `--your-name`: Your name for PDF footer
- `--your-phone`: Your phone for PDF footer
- `--your-email`: Your email for PDF footer
- `--delay`: Seconds between reports (default: 1.0)
- `--demo`: Generate demo reports

**Output:**
- Creates `reports/bulk_TIMESTAMP/` folder
- One PDF per business
- Named: `audit_[business_name].pdf`

**Pro tips:**
- Generate reports in batches of 20-30
- Use consistent contact info
- Review 1-2 samples before sending all
- Keep reports folder organized by date/campaign

### 3. Email Outreach System

**Templates:** `templates/email_outreach.md`

**Manual Process:**
1. Open leads CSV
2. Copy email template
3. Personalize:
   - [OWNER NAME] → Find on website or LinkedIn
   - [BUSINESS NAME] → From CSV
   - [CITY] → From CSV
   - [INDUSTRY] → From CSV
   - [SPECIFIC ISSUE] → From audit report
4. Attach their PDF report
5. Send
6. Log in tracking spreadsheet

**Semi-Automated with GMass:**
1. Install GMass Chrome extension
2. Open Google Sheet with leads
3. Create email template with merge fields:
   ```
   Hi {{owner_name}},

   I was researching local {{industry}} businesses in {{city}}...

   [Rest of template]
   ```
4. Map merge fields to columns
5. Attach PDFs (GMass can do this!)
6. Schedule sends
7. Auto follow-up sequences

**Recommended tools:**
- **GMass** ($25/mo) - Best for Gmail users
- **Lemlist** ($59/mo) - Best features, analytics
- **Reply.io** ($70/mo) - Best for teams
- **Mailchimp** (Free tier) - Basic but works

### 4. Landing Page (`landing-page/index.html`)

**Purpose:** Capture inbound leads 24/7

**Setup:** (See `landing-page/README.md`)
1. Deploy to Netlify/Vercel/GitHub Pages (free)
2. Connect form to Formspree or Google Sheets
3. Share URL everywhere

**Traffic sources:**
- Email signature
- Social media bios
- Facebook/Google Ads
- Business cards (QR code)
- LinkedIn posts
- Local SEO

**Expected conversion:** 15-25% of visitors
**Expected traffic:**
- Organic: 10-20 visitors/week
- With ads: 50-200 visitors/week

### 5. Social Media Automation

**Content:** `marketing/social-media-content.md`

**Manual posting (Week 1-2):**
- Copy pre-written posts
- Customize with your city/info
- Post 3-5x per week
- Engage with comments

**Automated posting (Week 3+):**

**Tools:**
- **Buffer** (Free) - Schedule posts
- **Hootsuite** (Free tier) - Multi-platform
- **Later** (Free) - Instagram focus

**Setup:**
1. Sign up for Buffer/Hootsuite
2. Connect social accounts
3. Load all posts from social-media-content.md
4. Schedule: Mon/Wed/Fri 10am-2pm
5. Set to repeat monthly

**Time investment:** 1 hour to set up, 0 hours ongoing

### 6. Paid Ads

**Templates:** `marketing/paid-ads-templates.md`

**Quick setup:**
1. Create Facebook Business Manager
2. Set up ad account
3. Create campaign (Lead Generation)
4. Use templates for ad copy
5. Budget: $10-20/day
6. Target: Your city, 30-65 age, business owners

**Expected:**
- Cost per lead: $2-5
- Leads per day: 3-10
- Time to setup: 1 hour
- Time to manage: 15 min/day

---

## 📅 SAMPLE AUTOMATION SCHEDULE

### Week 1: Manual Testing

**Monday:**
- 9am: Run lead_finder.py (30 min)
- 10am: Generate bulk audits (20 min)
- 11am: Send 10 emails manually (1 hour)
- 2pm: Post on LinkedIn (10 min)

**Tuesday-Friday:**
- Repeat Mon schedule
- Respond to email replies
- Close 1-2 clients

**Results:** 40 emails sent, 8 responses, 2 clients = $358

### Week 2-3: Semi-Automation

**Monday:**
- Find 100 leads (30 min)
- Generate 30 reports (10 min)
- Set up GMass sequence (1 hour)
- Launch Facebook ads (1 hour)

**Tuesday-Friday:**
- Check ad performance (15 min)
- Respond to leads (1 hour)
- Close clients (as needed)

**Results:** 150 emails sent, 100 ad leads, 30 responses, 6 clients = $1,074

### Week 4+: Full Automation

**Monday only:**
- Review metrics (30 min)
- Approve automated campaigns (15 min)
- Optimize ads (30 min)

**Daily:**
- Respond to leads (1-2 hours)
- Close clients (as needed)
- Deliver services

**Results:** 200+ leads/week, 10-20 responses, 5-10 clients = $895-1,790/week

**Your system is now running on autopilot!** 🚀

---

## 💰 ROI BREAKDOWN

### Time Investment

| Phase | Time/Week | Leads/Week | Clients/Week | Revenue/Week | Hourly Rate |
|-------|-----------|------------|--------------|--------------|-------------|
| Manual (Week 1) | 20 hours | 20 | 2 | $358 | $18/hr |
| Semi-Auto (Week 2-3) | 15 hours | 50 | 4 | $716 | $48/hr |
| Full Auto (Week 4+) | 10 hours | 100 | 6 | $1,074 | $107/hr |

**Goal:** Get to full automation ASAP

### Cost Breakdown

**Tools needed:**
- Lead finder: FREE (or $0 with API)
- Bulk audit: FREE
- Email outreach: $0-25/mo
- Landing page: FREE
- Social scheduler: FREE
- Facebook Ads: $70-140/week

**Total investment:** $70-200/week
**Expected revenue:** $700-1,500/week
**Net profit:** $500-1,300/week

**ROI:** 250-650%

---

## 🎯 SCALING ROADMAP

### Month 1: Build Foundation
- Set up all tools
- Test on 100 leads
- Get 5-10 clients
- Refine processes

### Month 2: Automate Outreach
- Set up email automation
- Launch landing page
- Start Facebook ads
- 15-20 clients

### Month 3: Scale Traffic
- Increase ad budget
- Hire VA for email research
- Post social media daily
- 30+ clients

### Month 4: Build Team
- Hire photographer ($20/hr)
- Hire profile manager ($15/hr)
- Focus on sales only
- 50+ clients

### Month 6: Full Business
- Team handles delivery
- You handle sales & strategy
- $10K+ MRR
- Consider SaaS

---

## 🔧 ADVANCED AUTOMATION

### Zapier Workflows

**Example 1: Landing Page → Email Sequence**
1. Lead fills form on landing page
2. Zapier catches submission
3. Adds to Google Sheet
4. Sends welcome email
5. Waits 2 days
6. Sends follow-up
7. Notifies you if they reply

**Example 2: Lead Finder → Auto Audit → Auto Email**
1. Run lead_finder.py daily (cron job)
2. Zapier monitors leads folder
3. Triggers bulk_audit.py
4. Waits for PDFs
5. Sends personalized email via GMass
6. Logs in CRM

**Cost:** $20/mo
**Value:** 10+ hours saved per week

### Make.com (formerly Integromat)

Similar to Zapier but more powerful for complex workflows.

**Use case:** Complete lead-to-client automation
- Find leads → Score → Audit → Email → Follow-up → Book meeting → Close

---

## ⚠️ IMPORTANT NOTES

### Email Best Practices
- Don't send >50 emails/day from one account (spam filters)
- Warm up new email accounts gradually
- Use professional domain (not Gmail)
- Track opens/clicks to improve
- Clean list of bounces

### API Rate Limits
- Google Places: 1 request per second
- Don't abuse API or you'll get banned
- Use delays in bulk_audit.py
- Monitor usage in Google Console

### Legal Compliance
- CAN-SPAM Act: Include unsubscribe link
- GDPR: If targeting EU, need consent
- CCPA: California privacy law
- Privacy policy on landing page

---

## 🆘 TROUBLESHOOTING

**"Lead finder returns no results"**
- Check API key is valid
- Try different industry/location
- Use --demo mode to test
- Lower --min-score threshold

**"Bulk audit fails"**
- Check CSV file format
- Ensure all required columns exist
- Try with --demo first
- Check Python dependencies installed

**"Emails going to spam"**
- Warm up email account
- Avoid spam trigger words
- Include unsubscribe link
- Send from business domain
- Don't use attachments (link to PDFs instead)

**"Low landing page conversions"**
- Simplify form (fewer fields)
- Add social proof/testimonials
- Test different headlines
- Make value prop clearer
- Add urgency/scarcity

**"Ads not performing"**
- Narrow targeting
- Test different creatives
- Check ad copy against templates
- Verify conversion tracking
- Give it 2-3 weeks minimum

---

## ✅ AUTOMATION CHECKLIST

**Week 1:**
- [ ] Test lead_finder.py in demo mode
- [ ] Generate 5 test audit reports
- [ ] Send 10 manual emails
- [ ] Deploy landing page
- [ ] Post on social media 3x

**Week 2:**
- [ ] Run lead_finder with real data (or demo)
- [ ] Generate 30 bulk audits
- [ ] Set up GMass/email tool
- [ ] Launch Facebook ad campaign ($10/day)
- [ ] Schedule social media posts

**Week 3:**
- [ ] Automate email sequences
- [ ] Optimize ads based on data
- [ ] Add retargeting pixels
- [ ] Set up Zapier workflows
- [ ] Track all metrics

**Week 4:**
- [ ] Scale profitable channels
- [ ] Turn off non-performers
- [ ] Hire VA for research/admin
- [ ] Document your processes
- [ ] Focus on delivery & sales

---

## 📊 METRICS TO TRACK

**Daily:**
- New leads (from each source)
- Emails sent
- Email open rate
- Responses received
- Meetings booked

**Weekly:**
- Total leads
- Lead → Client conversion rate
- Revenue
- Ad spend
- ROI

**Monthly:**
- MRR (monthly recurring revenue)
- Customer acquisition cost (CAC)
- Lifetime value (LTV)
- Churn rate
- Net profit

**Goal metrics:**
- CAC < $50
- LTV > $500
- LTV:CAC ratio > 3:1
- Email open rate > 40%
- Landing page conversion > 15%

---

## 🎉 YOU'RE READY TO AUTOMATE!

**You now have:**
✅ Lead finding tool
✅ Bulk audit generator
✅ Email outreach templates
✅ Landing page for inbound leads
✅ Social media content (30+ days)
✅ Paid ad templates
✅ Complete automation roadmap

**Start with manual, move to automated, scale to full business.**

**Timeline:**
- Week 1: Manual testing
- Week 2-3: Semi-automation
- Week 4+: Full automation
- Month 3: Hire team
- Month 6: Business runs itself

**This is how you go from $0 to $10K/mo in 6 months.**

**Now go build it! 🚀**
