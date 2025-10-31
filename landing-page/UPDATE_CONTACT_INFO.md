# Update Contact Information

## Quick Reference: Where to Update Your Contact Info

After you get your real phone number and email, update these placeholders:

### 1. In `index.html` (4 locations)

Search for these and replace with your real info:

**Phone Number:** `(208) 555-1234`
- Line ~472 (Footer section)

**Email Address:** `weber@apexlocalmarketing.com`
- Line ~474 (Footer section)

**Your Name:** `Weber`
- Line ~471 (Footer section)

**Location:** `Serving North Idaho`
- Line ~475 (Footer section - update if needed)

### 2. How to Update (Windows)

**Method 1: Using Notepad (Easy)**
1. Open File Explorer → `D:\gbp-tune-up-business\landing-page\`
2. Right-click `index.html` → Open with Notepad
3. Press `Ctrl+H` (Find & Replace)
4. Find: `(208) 555-1234`
5. Replace with: Your real phone number
6. Click "Replace All"
7. Repeat for email and name
8. Save (`Ctrl+S`)

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

### Recommended Domains for "Apex Local Marketing":
- **apexlocalmarketing.com** - $12/year
- **apexlocal.co** - $20/year
- **apexidaho.com** - $12/year

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
| Phone | (208) 555-1234 | [Get Google Voice number] |
| Email | weber@apexlocalmarketing.com | [Your real email] |
| Name | Weber | [Your name] |
| Domain | mellifluous-torrone-836797.netlify.app | [Buy apexlocalmarketing.com] |

---

## Contact Info Checklist

Before going live:
- [ ] Get real phone number (Google Voice or OpenPhone)
- [ ] Update phone in `index.html` (1 location)
- [ ] Update email in `index.html` (1 location)
- [ ] Update name if needed
- [ ] Test contact form submission
- [ ] Test phone number (call it, make sure it forwards)
- [ ] Test email (send test email, make sure you receive it)
- [ ] Deploy to Netlify
- [ ] Test live website
- [ ] (Optional) Buy domain and connect to Netlify

---

## Pro Tips

1. **Use Google Voice initially** - It's free and you can upgrade later
2. **Test everything** before sending emails to leads
3. **Update .env file too** (in project root) with your contact info
4. **Get a professional email** - Gmail is fine, but `weber@apexlocalmarketing.com` looks better
5. **Set up email forwarding** - Once you have a domain, create email forwards

---

## Questions?

All your files are in: `D:\gbp-tune-up-business\landing-page\`

- **Main website:** `index.html`
- **Styles:** `styles.css`
- **JavaScript:** `script.js`
- **This guide:** `UPDATE_CONTACT_INFO.md`

Make updates → Deploy → Test → Done!
