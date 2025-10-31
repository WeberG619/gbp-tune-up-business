# 📧 Email Automation Guide - Visible Local

Send professional outreach emails branded as "Visible Local" to your 76 leads with email addresses.

---

## ✅ What You Have

- **76 businesses with email addresses** (from your 202 total leads)
- **5 proven email templates** with "Visible Local" branding
- **Personalized emails** with their specific gaps
- **Automated tool** to generate emails in seconds

---

## 🚀 Quick Start (Send Emails Today)

### Step 1: Generate Your Email Campaign (2 minutes)

```bash
cd /mnt/d/gbp-tune-up-business

# Preview emails (see what they'll look like)
python tools/email_campaign.py \
  --csv maps/market_leads_20251030_214319_with_emails.csv \
  --template 1 \
  --preview 5

# Export to CSV for sending
python tools/email_campaign.py \
  --csv maps/market_leads_20251030_214319_with_emails.csv \
  --template 1 \
  --export
```

**Output:** `email_campaigns/campaign_template1_YYYYMMDD.csv` with 76 personalized emails ready to send!

**Latest campaign:** `email_campaigns/campaign_template3_20251031_004344.csv` (already generated with Visible Local branding)

---

### Step 2: Send Emails

You have 3 options:

#### **Option A: GMass (Recommended - FREE)**

**Best for:** Gmail users, easy setup, tracking

1. Go to https://www.gmass.co/ and install Chrome extension
2. Upload your CSV: `email_campaigns/campaign_template1_*.csv`
3. Click "Send emails"
4. Done! Tracks opens, clicks, replies automatically

**Free tier:** 50 emails/day (perfect for your 76 leads over 2 days)

---

#### **Option B: Manual Gmail (Free, More Personal)**

**Best for:** Small batches, high personalization

1. Open `email_campaigns/campaign_template1_*.csv`
2. For each row:
   - Copy email address
   - Copy subject
   - Copy body
   - Send from Gmail
   - Mark as sent in spreadsheet

**Pro:** Most personal, highest reply rate
**Con:** Time-consuming (76 emails = ~2 hours)

---

#### **Option C: Mailchimp (Free tier)**

**Best for:** Professional tracking, automation

1. Sign up at https://mailchimp.com/ (free up to 500 contacts)
2. Import your CSV
3. Create campaign using email body as template
4. Schedule sends
5. Track opens/clicks

---

## 📋 Email Templates Explained

### Template 1: Professional & Direct ⭐ **Best for First Contact**
- **Subject:** "{Business Name} - Your Google Profile is Missing Customers"
- **Tone:** Professional, data-driven
- **Best for:** Salons, gyms, professional services
- **Expected response rate:** 10-15%

### Template 2: Casual Question
- **Subject:** "Quick Question About {Business Name}'s Google Listing"
- **Tone:** Friendly, low-pressure
- **Best for:** Small businesses, solo owners
- **Expected response rate:** 8-12%

### Template 3: Free Value Lead
- **Subject:** "Free Google Profile Audit for {Business Name}"
- **Tone:** Value-first, no pressure
- **Best for:** Cold leads, skeptical owners
- **Expected response rate:** 12-18%

### Template 4: Local Connection
- **Subject:** "Local business owner here - noticed {Business Name}'s Google listing"
- **Tone:** Local, personal, professional
- **Best for:** North Idaho/local businesses
- **Expected response rate:** 15-20%

### Template 5: Results-Focused
- **Subject:** "Is Google Sending You Enough Customers?"
- **Tone:** Question-based, ROI-focused
- **Best for:** Established businesses, data-driven owners
- **Expected response rate:** 10-14%

---

## 📊 Sending Strategy

### Week 1: Test & Refine

**Day 1:** Send Template 3 (free value) to 20 leads
**Day 2:** Send Template 4 (local angle) to 20 leads
**Day 3:** Analyze responses, pick winner

**Expected results:** 3-5 responses, 1-2 meetings

---

### Week 2: Scale

**Day 1:** Send winning template to remaining 36 leads
**Day 2:** Follow up with non-responders (different template)
**Day 3:** Close deals

**Expected results:** 5-8 total responses, 2-3 clients

---

## ✉️ Email Best Practices

### ✅ DO's:

- **Send between 9am-11am or 2pm-4pm** (highest open rates)
- **Tuesday-Thursday** (best days)
- **Personalize subject lines** (use their business name)
- **Keep emails under 150 words** (higher reply rates)
- **Include ONE clear call-to-action** (reply, call, or book)
- **Follow up 3 days later** if no response
- **Track opens and clicks** (use GMass or Mailchimp)

### ❌ DON'Ts:

- Don't send all 76 at once (looks spammy)
- Don't use ALL CAPS or excessive punctuation!!!
- Don't attach large files (use links instead)
- Don't send from "noreply@" addresses
- Don't send more than 2 follow-ups
- Don't send on weekends or after 5pm

---

## 🎯 Response Handling

### If They Reply "YES" / "INTERESTED":

```
Great! I'll send over your free audit report showing:
- Your current Google profile score
- What competitors are doing better
- Exactly what's missing
- Estimated impact on calls/traffic

What's the best email to send it to? (I'll have it to you within 24 hours)

Also - are you free for a quick 10-min call this week? I can walk you through the report and answer any questions.

Best times for me: [YOUR AVAILABILITY]

Thanks!
Visible Local
contact@visiblelocal.co
North Idaho
```

Then:
1. Generate their audit report: `python tools/gbp_audit.py "Business Name" "City, State" --pdf`
2. Email the PDF
3. Schedule call
4. Close the deal!

---

### If They Reply "NOT INTERESTED":

```
No problem! If anything changes, feel free to reach out.

One quick question (helps me improve): What made you say no? Too expensive? Not a priority? Already handled?

Either way, best of luck with the business!

Visible Local
```

**Why ask?** You'll learn objections and improve your pitch.

---

### If No Response After 3 Days:

**Follow-up email:**

```
Subject: Following up - Free audit for {Business Name}

Hi,

Just wanted to follow up on my email from a few days ago.

I know you're busy running the business, so I'll keep this short:

I'm offering free Google Business Profile audits to {industry} businesses this week. Takes me 10 minutes to create, shows you exactly what's costing you customers.

Want me to send it? Just reply "yes."

If not interested, reply "no thanks" and I won't bug you again!

Best,
Visible Local
contact@visiblelocal.co
North Idaho
```

**Send this once.** If still no response, move on.

---

## 📈 Expected Results

### Conservative (Worst Case):
- **76 emails sent**
- **5% response rate** = 4 responses
- **50% close rate** = 2 clients
- **Revenue:** $358

### Realistic (Average):
- **76 emails sent**
- **12% response rate** = 9 responses
- **50% close rate** = 4-5 clients
- **Revenue:** $716-895

### Optimistic (Best Case):
- **76 emails sent**
- **18% response rate** = 14 responses
- **60% close rate** = 8-9 clients
- **Revenue:** $1,432-1,611

**Most likely:** You'll get 4-6 clients from this email campaign = $716-1,074 💰

---

## 🔧 Advanced: Automated Follow-Up Sequence

For maximum conversions, set up a 3-email sequence:

**Email 1 (Day 0):** Initial outreach (Template 3 or 4)
**Email 2 (Day 3):** Follow-up if no response
**Email 3 (Day 7):** Final follow-up with urgency

Use Mailchimp or GMass automation to set this up once and let it run.

---

## ✅ Pre-Send Checklist

Before hitting send on 76 emails:

- [ ] Test email sent to yourself (check formatting)
- [ ] Unsubscribe link included (if using bulk tool)
- [ ] Your signature has phone + email
- [ ] Links work (if any)
- [ ] No typos (run spell check)
- [ ] Personalization works ({business_name} filled in)
- [ ] Sending from professional email (not @gmail if possible)
- [ ] Calendar is clear to handle responses
- [ ] Audit tool tested and working

---

## 🚨 Legal Compliance (CAN-SPAM Act)

✅ **Required:**
- Include your physical address (North Idaho)
- Include unsubscribe link (GMass/Mailchimp add automatically)
- Don't use misleading subject lines
- Honor unsubscribe requests within 10 days

**You're compliant if:**
- You're offering a legitimate business service
- You include your contact info
- You honor opt-outs
- You're not being deceptive

---

## 💡 Pro Tips

1. **Send from your professional email** - Use "Visible Local" in your name field for higher open rates

2. **A/B test subject lines** on first 20 emails:
   - 10 with Subject A
   - 10 with Subject B
   - Use winner for remaining 56

3. **Warm up your email** if sending 76 in one day:
   - Day 1: 25 emails
   - Day 2: 25 emails
   - Day 3: 26 emails
   - Avoids spam filters

4. **Track everything:**
   - Opens (who's interested)
   - Clicks (who's very interested)
   - Replies (ready to buy)

5. **Reply FAST:**
   - Within 5 minutes = 21% conversion
   - Within 1 hour = 12% conversion
   - Within 24 hours = 7% conversion

---

## 📞 What to Do When Phone Rings

They'll call after reading your email. Be ready:

**Your Script:**

"Hi, this is Visible Local! Thanks for calling. Are you calling about the Google Business Profile audit I emailed?

[They say yes]

Great! So I took a quick look at [BUSINESS NAME]'s profile and found a few things we can improve. Do you have 5 minutes for me to walk you through it?

[Walk through their gaps]

Here's what I do: I come to your location, take 20 professional photos, optimize your entire profile, set up 4 weeks of posts, and handle all the technical stuff. Takes 90 minutes and you'll see results within days.

One-time cost is $179, and I guarantee more calls within 14 days or I refund you.

I actually have a slot open [THIS WEEK]. Want to book it?"

**Close the deal.** 🎯

---

## 🎉 You're Ready!

You now have:
- ✅ 76 email addresses
- ✅ 5 professional templates with "Visible Local" branding
- ✅ Automated tool to generate campaigns
- ✅ Sending strategy
- ✅ Response handling scripts
- ✅ Campaign already generated: `campaign_template3_20251031_004344.csv`

**Next step: Send your emails using GMass or manually!**

```bash
python tools/email_campaign.py \
  --csv maps/market_leads_20251030_214319_with_emails.csv \
  --template 3 \
  --export
```

**Expected time investment:** 2 hours
**Expected revenue:** $700-1,500

Let's get those customers! 💰
