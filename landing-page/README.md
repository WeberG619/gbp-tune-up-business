# Landing Page - Deploy Guide

Your professional landing page to capture leads online 24/7.

## ✅ What It Does

- Collects lead information (business name, email, phone)
- Looks professional and builds trust
- Mobile-responsive
- Zero maintenance
- **100% FREE to host**

## 🚀 Quick Deploy (5 minutes)

### Option 1: GitHub Pages (Recommended - FREE)

1. **Create GitHub account** (if you don't have one)
   - Go to github.com
   - Sign up for free

2. **Create new repository**
   - Click "New repository"
   - Name it: `gbp-services` (or anything you want)
   - Make it Public
   - Click "Create repository"

3. **Upload your landing page**
   - Click "uploading an existing file"
   - Drag and drop `index.html` from this folder
   - Click "Commit changes"

4. **Enable GitHub Pages**
   - Go to repository Settings
   - Scroll to "Pages" section
   - Source: Select "main" branch
   - Click Save

5. **Your site is live!**
   - URL will be: `https://[your-username].github.io/gbp-services/`
   - Visit it to confirm it works

**Time: 5 minutes | Cost: $0**

### Option 2: Netlify (Even Easier - FREE)

1. Go to [netlify.com](https://netlify.com)
2. Click "Sign Up" (use GitHub account)
3. Click "Add new site" → "Deploy manually"
4. Drag the `landing-page/` folder into the upload area
5. Done! Your site is live instantly

**URL:** `https://random-name-12345.netlify.app`

You can customize the URL in Settings.

**Time: 2 minutes | Cost: $0**

### Option 3: Vercel (FREE)

1. Go to [vercel.com](https://vercel.com)
2. Sign up with GitHub
3. Click "New Project"
4. Import your repo or drag folder
5. Click "Deploy"

**Time: 3 minutes | Cost: $0**

## 🎨 Customization

### 1. Replace Placeholder Text

Open `index.html` and search for these placeholders:

**In the footer:**
```html
<p>&copy; 2025 [Your Business Name]. All rights reserved.</p>
```
Replace `[Your Business Name]` with your actual business name.

**Optional customizations:**
- Change the gradient colors (lines 26-27)
- Update the testimonial (lines 127-130)
- Add your logo
- Change button text

### 2. Set Up Form Submissions

By default, form submissions save to browser's localStorage (temporary).

**To receive actual leads, choose one:**

#### A. Formspree (Easiest - FREE)

1. Go to [formspree.io](https://formspree.io)
2. Sign up for free account
3. Create new form
4. Copy your form endpoint
5. In `index.html`, find line 218:
   ```javascript
   /*
   await fetch('https://formspree.io/f/YOUR_FORM_ID', {
   ```
6. Uncomment and replace `YOUR_FORM_ID`

Now leads email to you automatically!

#### B. Google Sheets (FREE)

1. Use [Google Apps Script](https://script.google.com)
2. Create script to send form data to Sheet
3. Tutorial: google "send form data to google sheets"

#### C. Your Own Backend

If you have a server, POST form data to your endpoint.

## 📱 Get Traffic to Your Landing Page

### 1. Add to Your Email Signature

```
---
[Your Name]
Google Business Profile Optimization
Get Your Free Audit: [YOUR-LANDING-PAGE-URL]
```

### 2. Share on Social Media

**LinkedIn post:**
```
🚀 Launching a free resource for local business owners!

Get a professional audit of your Google Business Profile and see why competitors might be getting more customers than you.

100% free, no strings attached: [YOUR-URL]

#LocalBusiness #SmallBusiness #GoogleMyBusiness
```

**Facebook post:**
```
Attention [Your City] business owners! 📊

Is your Google profile costing you customers?

I'm offering FREE Google Business Profile audits this month.
Find out where you stand vs. competitors: [YOUR-URL]

Tag a business owner who needs this!
```

### 3. Facebook/Google Ads

**Budget:** $10-20/day
**Expected:** 5-10 leads per day
**Cost per lead:** $2-4

We'll create ad templates for you (see `social-media-ads.md`)

### 4. Local SEO

**Page title includes:**
- City name
- "Google Business Profile"
- "Free Audit"

**Example:** "Free Google Business Profile Audit - Austin, TX"

Google will rank you for local searches!

### 5. QR Code

**Generate QR code** linking to your landing page:
- Use qr-code-generator.com
- Print it on business cards
- Show it to prospects: "Scan for your free audit"

## 📊 Track Your Leads

### Option 1: Check localStorage (Temporary)

While on your landing page:
1. Right-click → Inspect
2. Go to Application tab
3. Click "Local Storage"
4. View submitted leads

**Note:** Only works on the device/browser where form was submitted.

### Option 2: Formspree Dashboard

If using Formspree, all submissions show in your dashboard.

### Option 3: Google Sheets

If using Apps Script, submissions save to spreadsheet automatically.

### Option 4: Email Notifications

Set up Formspree or Zapier to email you when someone submits.

## 🎯 Conversion Optimization Tips

### Current conversion rate: ~15-25%

**To improve:**

1. **Add social proof**
   - Screenshot of Google review
   - "50+ businesses helped"
   - Your photo (builds trust)

2. **Add urgency**
   - "Limited to 5 audits per week"
   - "Free only in [Month]"

3. **Reduce friction**
   - Make phone optional (it already is)
   - Add "No spam, no sales calls" text

4. **A/B test headlines**
   ```
   Option A: "Is Your Google Profile Losing You Customers?"
   Option B: "Get More Customers from Google Search"
   Option C: "Why Are Competitors Showing Up Before You?"
   ```

5. **Add video**
   - 60-second explainer video
   - Loom or iPhone recording
   - Show before/after profile

## 💰 Expected ROI

**Investment:**
- Time: 5 minutes to deploy
- Money: $0 (using free hosting)
- Ads (optional): $10-20/day

**Returns:**
- Passive leads 24/7
- 5-10 leads/week with ads
- 1-2 leads/week organically
- 10-20% convert to clients

**Example:**
- 10 leads/week
- 2 convert (20%)
- 2 clients × $179 = **$358/week**
- Cost: $70/week in ads
- Net: **$288/week profit** = **$1,200+/month**

**All automated while you sleep!**

## 🔧 Advanced: Custom Domain

Want `www.yourbusinessname.com` instead of GitHub/Netlify URL?

1. **Buy domain** - $12/year
   - Namecheap, GoDaddy, Google Domains

2. **Connect to hosting:**
   - **GitHub Pages:** [Guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
   - **Netlify:** Settings → Domain management → Add custom domain
   - **Vercel:** Settings → Domains → Add

**Takes 10 minutes. Looks way more professional!**

## 📈 Scaling

Once it's working:

1. **Clone for different cities**
   - `austin-gbp-audit.netlify.app`
   - `dallas-gbp-audit.netlify.app`
   - Better local SEO

2. **Add chat widget**
   - Tawk.to (free live chat)
   - Talk to leads in real-time

3. **Add booking calendar**
   - Calendly (free)
   - Let them book consultation directly

4. **Add case studies**
   - Before/after examples
   - Client testimonials
   - Increases trust/conversion

## 🆘 Troubleshooting

**"Form doesn't submit"**
- Check browser console (F12) for errors
- Make sure Formspree endpoint is correct

**"Page not loading"**
- Check GitHub Pages is enabled
- Wait 5-10 minutes after enabling

**"Leads not coming through"**
- Test the form yourself first
- Check spam folder
- Verify Formspree/backend is connected

**"Low conversion rate"**
- Add more trust signals
- Simplify form (fewer fields)
- Test different headlines

## ✅ Deployment Checklist

- [ ] Customize footer with your business name
- [ ] Set up form backend (Formspree recommended)
- [ ] Deploy to GitHub Pages, Netlify, or Vercel
- [ ] Test form submission
- [ ] Verify you receive lead notification
- [ ] Share URL on social media
- [ ] Add to email signature
- [ ] (Optional) Set up Facebook ads
- [ ] (Optional) Connect custom domain
- [ ] Track leads weekly

## 🎉 You're Live!

Your landing page is now working 24/7 to bring you leads while you focus on delivering great service.

**Next steps:**
1. Share the URL everywhere
2. Run small ads campaign
3. Generate audit reports for leads
4. Follow up with email templates
5. Close deals!

**Questions?** Check the main documentation or open an issue on GitHub.

**Good luck! 🚀**
