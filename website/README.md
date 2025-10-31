# GBP Tune-Up Website

Professional landing page for your Google Business Profile optimization service.

## 🎨 What's Included

- **Modern, responsive design** - Works perfectly on desktop, tablet, and mobile
- **Conversion-optimized layout** - Clear CTAs, social proof, and pricing
- **Professional styling** - Clean, modern design that builds trust
- **Contact form** - Ready for integration with your backend
- **Smooth animations** - Professional scroll effects and interactions

## 🚀 Quick Setup

### Option 1: Deploy to Free Hosting

#### Netlify (Recommended - Easiest)

1. Go to [Netlify](https://www.netlify.com/)
2. Sign up for free account
3. Drag and drop the `website` folder onto Netlify
4. Your site is live! (e.g., `your-site.netlify.app`)
5. Connect custom domain (optional)

#### Vercel

1. Go to [Vercel](https://vercel.com/)
2. Sign up for free account
3. Import from Git or upload `website` folder
4. Your site is live! (e.g., `your-site.vercel.app`)

#### GitHub Pages (Free)

1. Create new repo: `your-username.github.io`
2. Upload all files from `website` folder
3. Go to Settings → Pages
4. Select branch and save
5. Your site is live at `https://your-username.github.io`

### Option 2: Traditional Web Hosting

1. Get hosting (Bluehost, SiteGround, NameCheap, etc.)
2. Upload all files via FTP
3. Point your domain to the files
4. Done!

## ⚙️ Customization Guide

### 1. Update Contact Information

**File:** `index.html`

Find and replace:
- `YOUR PHONE NUMBER` → Your actual phone number (3 places)
- `YOUR EMAIL` → Your actual email address (3 places)
- `Your City & Surrounding Areas` → Your service area
- `YOUR CITY, STATE` → Your location

### 2. Add Your Phone/Email Links

Update these lines in `index.html`:

```html
<!-- Line ~662 -->
<a href="tel:YOUR_PHONE" class="contact-link">YOUR PHONE NUMBER</a>

<!-- Line ~668 -->
<a href="mailto:YOUR_EMAIL" class="contact-link">YOUR EMAIL</a>
```

Replace:
- `tel:YOUR_PHONE` → `tel:2081234567` (your actual number, no spaces/dashes)
- `mailto:YOUR_EMAIL` → `mailto:your@email.com`

### 3. Configure Contact Form

The form currently shows an alert. To make it actually send emails:

**Option A: Use Formspree (Easiest)**

1. Go to [Formspree](https://formspree.io/)
2. Create free account and get your form endpoint
3. In `index.html`, line ~686, update:

```html
<form class="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

4. Remove the form handler in `script.js` (lines 15-41)

**Option B: Use Google Forms**

1. Create Google Form
2. Get the form action URL
3. Update form in `index.html`

**Option C: Build Backend**

See `BACKEND_SETUP.md` for Node.js/PHP examples

### 4. Add Google Analytics (Optional)

Add before `</head>` in `index.html`:

```html
<!-- Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=YOUR-GA-ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'YOUR-GA-ID');
</script>
```

### 5. Update Results/Testimonials

Edit the results in `index.html` (lines ~450-520) with your actual client results.

## 📱 Mobile Responsiveness

The site is fully responsive and tested on:
- iPhone (all sizes)
- Android phones
- Tablets (iPad, Android)
- Desktop (all screen sizes)

## 🎨 Color Customization

Want to change the color scheme? Edit `style.css` lines 12-18:

```css
:root {
    --primary: #2563eb;        /* Main blue */
    --primary-dark: #1d4ed8;   /* Darker blue for hovers */
    --secondary: #10b981;      /* Green for accents */
    --dark: #1f2937;           /* Text color */
    --light: #f9fafb;          /* Background color */
    --gray: #6b7280;           /* Secondary text */
    --border: #e5e7eb;         /* Border color */
}
```

Change these hex codes to your brand colors.

## 🔧 Technical Details

- **No frameworks required** - Pure HTML, CSS, JavaScript
- **Fast loading** - Under 50KB total
- **SEO optimized** - Proper meta tags, semantic HTML
- **Accessible** - WCAG compliant
- **Cross-browser** - Works in all modern browsers

## 📊 Tracking Conversions

Add tracking to your contact form submissions and phone clicks:

1. Use Google Analytics events
2. Use Facebook Pixel (if running ads)
3. Use call tracking service (CallRail, CallTrackingMetrics)

## 🚀 Next Steps

1. ✅ Upload to hosting
2. ✅ Update contact info
3. ✅ Configure form
4. ✅ Add Google Analytics
5. ✅ Test on mobile
6. ✅ Share URL on Google Business Profile
7. ✅ Add to email signatures
8. ✅ Use in marketing materials

## 💡 Pro Tips

### Use This Site To:

1. **Send to prospects** - Include link in cold emails
2. **In-person pitches** - Show on tablet during walkthrough
3. **Social media** - Post on Facebook, Instagram, LinkedIn
4. **Google Business Profile** - Add as your website URL
5. **Email signature** - Link in every email

### Conversion Boosters:

1. Add live chat (Tawk.to, Intercom - free options available)
2. Add before/after photo gallery
3. Collect video testimonials
4. Add "As seen in" local news logos (if applicable)
5. Create blog posts for SEO

## 🆘 Troubleshooting

### Site Not Loading?
- Check that all files are uploaded
- Verify file paths are correct
- Check browser console for errors

### Form Not Working?
- Make sure you configured the form action
- Check `script.js` for errors
- Test with Formspree first (easiest)

### Images Not Showing?
- This template uses emojis instead of images (faster, simpler)
- To add real images, replace emojis with `<img>` tags

### Mobile Menu Not Working?
- The script auto-creates mobile menu
- If issues, check browser console

## 📞 Support

Questions about the website?
- Check the main repository README
- Open an issue on GitHub
- Review `DEPLOYMENT_GUIDE.md` in the main repo

## 📄 License

MIT - Use it, modify it, make money with it. No attribution required.

---

**Your professional website is ready. Now get it live and start booking clients!** 🚀
