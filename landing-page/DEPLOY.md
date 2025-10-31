# 🚀 Landing Page Deployment Guide

Deploy your professional GBP Services website to Netlify in 5 minutes.

---

## ✅ What's Included

- **Professional landing page** with your branding (Weber, (208) 555-1234)
- **Contact form** that captures leads
- **Mobile responsive** design
- **SEO optimized** for local searches
- **Fast loading** (< 1 second)

---

## 🎯 Deployment Options

### Option 1: Update Existing Netlify Site (Recommended)

You already have a site at `mellifluous-torrone-836797.netlify.app`. Update it with this new design:

**Step 1: Package the files**

```bash
cd /mnt/d/gbp-tune-up-business/landing-page
zip -r gbp-landing-page.zip *
```

**Step 2: Deploy to Netlify**

1. Go to https://app.netlify.com/
2. Find your site: `mellifluous-torrone-836797`
3. Click **Deploys** tab
4. Drag and drop `gbp-landing-page.zip` into the deploy zone
5. Wait 30 seconds - done!

**Your site will be live at:** https://mellifluous-torrone-836797.netlify.app

---

### Option 2: Deploy from GitHub (Best for Updates)

**Step 1: Push landing page to GitHub**

```bash
cd /mnt/d/gbp-tune-up-business
git add landing-page/
git commit -m "Add professional landing page"
git push origin master
```

**Step 2: Connect to Netlify**

1. Go to https://app.netlify.com/
2. Click **Add new site** → **Import an existing project**
3. Choose **GitHub**
4. Select repository: `gbp-tune-up-business`
5. Build settings:
   - **Base directory:** `landing-page`
   - **Build command:** (leave empty)
   - **Publish directory:** `.`
6. Click **Deploy site**

**Result:** Any future changes you push to GitHub will auto-deploy! ✨

---

### Option 3: CLI Deployment (For Advanced Users)

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Login
netlify login

# Deploy
cd landing-page
netlify deploy --prod
```

---

## 🎨 Customization

### Update Your Contact Info

Edit these files with your real information:

**1. `index.html`** (Lines you need to update):
- Line 194: `weber@gbpservices.com` → Your real email
- Line 536: `(208) 555-1234` → Your real phone
- Line 544: `weber@gbpservices.com` → Your real email

**2. `.env` file** (Already updated with your info):
```
YOUR_NAME=Weber
YOUR_PHONE=(208) 555-1234
YOUR_EMAIL=your.email@gmail.com  ← Update this!
```

### Change Colors/Branding

Edit `styles.css`:
```css
:root {
    --primary: #4F46E5;  /* Your brand color */
    --secondary: #10B981;
}
```

---

## 📧 Form Submissions

The contact form currently saves leads to localStorage. To receive emails:

### Option A: Netlify Forms (Free, Easy)

1. Add this to your `<form>` tag in `index.html`:
```html
<form name="contact" method="POST" data-netlify="true">
```

2. Redeploy

3. Check form submissions at: https://app.netlify.com/sites/YOUR-SITE/forms

### Option B: Email Integration (Zapier)

1. Create free Zapier account
2. New Zap: **Netlify Form** → **Gmail**
3. Connect your site
4. Test!

### Option C: Direct Email (Requires Backend)

Use the email automation tool we'll set up next to send professional emails.

---

## 🔧 Testing Before Deployment

**Local preview:**

```bash
cd landing-page

# Python 3
python3 -m http.server 8000

# Or Python 2
python -m SimpleHTTPServer 8000

# Open browser: http://localhost:8000
```

**Check:**
- ✓ All links work
- ✓ Form submits
- ✓ Mobile responsive (resize browser)
- ✓ Contact info is correct

---

## 📊 Analytics Setup (Optional)

Add Google Analytics to track visitors:

**1. Get tracking ID:**
- Go to https://analytics.google.com/
- Create property
- Get tracking ID (G-XXXXXXXXXX)

**2. Add to `index.html` before `</head>`:**

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## 🎯 Custom Domain (Optional)

**Instead of `mellifluous-torrone-836797.netlify.app`, use `gbpservices.com`:**

1. Buy domain at Namecheap ($12/year)
2. In Netlify: **Domain settings** → **Add custom domain**
3. Update DNS (Netlify provides instructions)
4. Wait 24-48 hours for propagation

**Recommended domains:**
- gbpservices.com
- webergbp.com
- idahogbpservices.com

---

## ✅ Post-Deployment Checklist

After deploying, verify:

- [ ] Site loads at your Netlify URL
- [ ] Contact form works (submit a test)
- [ ] All images/styles load
- [ ] Mobile responsive (test on phone)
- [ ] Contact info is YOUR info (not placeholder)
- [ ] Links work (#services, #pricing, etc.)
- [ ] Forms email you (if using Netlify Forms)

---

## 🆘 Troubleshooting

**Site not loading?**
- Check Netlify deploy log for errors
- Make sure all files are in `landing-page/` folder

**Form not working?**
- Check `script.js` is loaded
- Open browser console (F12) for errors
- Try Netlify Forms integration (Option A above)

**Styling broken?**
- Clear browser cache (Ctrl+Shift+R)
- Check `styles.css` path is correct

---

## 🚀 What's Next?

1. **Deploy this landing page** ✅
2. **Set up email automation** (next step - see EMAIL_AUTOMATION.md)
3. **Start sending emails** to your 79 leads
4. **Get customers!** 💰

---

**Your site is ready to convert visitors into customers. Let's deploy it!** 🎯
