# Update Contact Information - Visible Local

## Quick Reference: Where to Update Your Contact Info

After you get your real phone number and email, update these placeholders:

### 1. In `index.html` (2 locations)

Search for these and replace with your real info:

**Email Address:** `contact@visiblelocal.co`
- Line 220 (Contact section)
- Line 273 (Footer section)

**Business Name:** Visible Local (already set)
**Location:** North Idaho (already set)

### 2. How to Update (Windows)

**Method 1: Using Notepad (Easy)**
1. Open File Explorer → `D:\gbp-tune-up-business\landing-page\`
2. Right-click `index.html` → Open with Notepad
3. Press `Ctrl+H` (Find & Replace)
4. Find: `contact@visiblelocal.co`
5. Replace with: `your.real.email@gmail.com`
6. Click "Replace All" (should replace 2 instances)
7. Save (`Ctrl+S`)

**Method 2: Using VS Code (Better)**
1. Open VS Code
2. Open folder: `D:\gbp-tune-up-business\landing-page\`
3. Open `index.html`
4. Press `Ctrl+H`
5. Replace all placeholders
6. Save

---

## Get a Real Phone Number (Before Updating)

### Option A: Google Voice (FREE - Recommended to Start)

**Setup (5 minutes):**
1. Go to https://voice.google.com
2. Sign in with Gmail
3. Click "Get Google Voice"
4. Search for 208 area code
5. Pick a number
6. Verify with your cell phone
7. Done! ✓

**Features:**
- Free forever
- Real 208 Idaho number
- Forwards to your cell
- Voicemail transcription
- Text messages
- Voicemail to email

**Perfect for:** Starting out, testing the service

---

### Option B: OpenPhone ($15/month - Professional)

**Setup (10 minutes):**
1. Go to https://www.openphone.com
2. Sign up
3. Choose 208 area code
4. Get a number
5. Download app (iPhone/Android)

**Features:**
- Professional business phone
- Shared inbox (team access)
- Auto-responses
- Business hours
- Call recording
- Analytics

**Perfect for:** When you have multiple clients and want professional features

---

## Get a Domain Name (Optional - When You're Ready)

### Recommended Domains for "Visible Local":
- **visiblelocal.com** - $12/year (Perfect match!)
- **visiblelocal.co** - $20/year (Modern alternative)
- **getvisible.local** - If .local TLD available

### Where to Buy:
- **Namecheap.com** - Cheapest, best interface
- **Porkbun.com** - Also cheap, good support
- Avoid GoDaddy (expensive renewals)

### How to Connect Domain to Netlify:
1. Buy domain at Namecheap
2. Go to Netlify dashboard → Domain settings
3. Click "Add custom domain"
4. Enter your domain
5. Follow DNS instructions from Netlify
6. Wait 24-48 hours for DNS propagation
7. Done!

---

## After You Update Contact Info

### 1. Test Locally (Optional)
```bash
cd /mnt/d/gbp-tune-up-business/landing-page
python3 -m http.server 8000
# Open browser: http://localhost:8000
```

### 2. Deploy to Netlify

**Method A: Drag & Drop (Easy)**
1. Open File Explorer: `D:\gbp-tune-up-business\landing-page\`
2. Select files: `index.html`, `styles.css`, `script.js`, `netlify.toml`
3. Go to: https://app.netlify.com/sites/mellifluous-torrone-836797/deploys
4. Drag files into deploy zone
5. Wait 30 seconds - live!

**Method B: Git Push (Better for updates)**
```bash
cd /mnt/d/gbp-tune-up-business
git add landing-page/
git commit -m "feat: update contact information"
git push origin master
```
Then Netlify auto-deploys (if connected to GitHub)

### 3. Test Your Live Site
- Visit: https://mellifluous-torrone-836797.netlify.app
- Test contact form (use your email)
- Call the phone number (make sure it forwards)
- Check mobile view (resize browser or use phone)

---

## Current Placeholders (Need to be Updated)

| Item | Current Placeholder | Your Real Info |
|------|-------------------|----------------|
| Email | contact@visiblelocal.co | [Your real email] |
| Business | Visible Local | ✓ Set |
| Phone | Optional | [Get Google Voice if needed] |
| Domain | mellifluous-torrone-836797.netlify.app | [Buy visiblelocal.com when ready] |

---

## Contact Info Checklist

Before going live:
- [ ] Update email in `index.html` (2 locations: lines 220 & 273)
- [ ] Optional: Get phone number (Google Voice or OpenPhone)
- [ ] Test contact form submission
- [ ] Test email (send test email, make sure you receive it)
- [ ] Deploy to Netlify
- [ ] Test live website
- [ ] (Optional) Buy domain visiblelocal.com and connect to Netlify

---

## Pro Tips

1. **Phone is optional** - You can start without a phone number, just use email
2. **Test everything** before sending emails to leads
3. **Update email campaigns** - All templates already use contact@visiblelocal.co, just update with your real email
4. **Get a professional email** - Gmail works fine, or get `contact@visiblelocal.com` once you buy the domain
5. **Set up email forwarding** - Once you have visiblelocal.com domain, create email forwards

---

## Questions?

All your files are in: `D:\gbp-tune-up-business\landing-page\`

- **Main website:** `index.html`
- **Styles:** `styles.css`
- **JavaScript:** `script.js`
- **This guide:** `UPDATE_CONTACT_INFO.md`

Make updates → Deploy → Test → Done!
