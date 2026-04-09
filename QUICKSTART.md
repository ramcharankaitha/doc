# 🚀 DataVault Secure - Quick Start Guide

Get your DataVault Secure platform running in under 2 minutes!

---

## ⚡ Super Quick Start

### **Option 1: Start Everything (Recommended)**
```bash
# From the root directory (doc-final)
python start.py
```

### **Option 2: Windows Batch File**
```bash
# Double-click or run from command prompt
start.bat
```

### **Option 3: Start Servers Separately**

**Backend:**
```bash
cd backend
python app.py
```

**Frontend (in new terminal):**
```bash
cd frontend  
python app.py
```

---

## 🌐 Access Your Application

Once started, open your browser and go to:

- **🏠 Landing Page:** http://localhost:3000/index.html
- **🔐 Login Page:** http://localhost:3000/login.html
- **📊 User Dashboard:** http://localhost:3000/dashboard.html
- **👨‍💼 Admin Panel:** http://localhost:3000/admin.html
- **🔧 Super Admin:** http://localhost:3000/superadmin.html

## 🔐 Administrator Accounts

| Role | Email | Password |
|------|-------|----------|
| Super Admin | `superadmin@datavault.com` | `SuperAdmin2024!` |
| Admin | `admin@datavault.com` | `Admin2024!` |

**Note:** Regular users must register through the application interface.

## 🛠️ API Testing

- **🚀 Backend API:** http://localhost:8001
- **📚 API Documentation:** http://localhost:8001/api/docs
- **🧪 Test Endpoint:** http://localhost:8001/api/test

---

## 📋 Prerequisites

- ✅ Python 3.7+ installed
- ✅ Modern web browser
- ✅ That's it! No additional setup required

---

## 🔧 Troubleshooting

### Port Already in Use
If you get port errors:
- Backend uses port 8001
- Frontend uses port 3000
- Make sure these ports are free

### Python Not Found
Make sure Python is installed and in your PATH:
```bash
python --version
```

### Dependencies Missing
The backend has a virtual environment with all dependencies pre-installed.

---

## 🎯 What's Next?

1. **Test the login** with the provided accounts
2. **Explore the dashboards** for different user roles
3. **Check the API documentation** at http://localhost:8001/api/docs
4. **Upload test documents** to see the security features

---

**🎉 You're all set! Your DataVault Secure platform is now running!**

## 🎯 Option 1: View Static Demo (Fastest)

### Step 1: Open the Files

Simply open the HTML files in your browser:

```bash
# Navigate to project folder
cd datavault-secure

# Open landing page
# Windows
start index.html

# Mac
open index.html

# Linux
xdg-open index.html
```

### Step 2: Navigate Between Dashboards

- **Landing Page:** `index.html`
- **User Dashboard:** `userdashbaord.html`
- **Admin Dashboard:** `admindashboard.html`
- **Super Admin:** `superadmin.html`

All navigation links are already connected!

---

## 🔧 Option 2: Local Development Server

### Step 1: Install Live Server

**Using VS Code:**
1. Install "Live Server" extension
2. Right-click `index.html`
3. Select "Open with Live Server"

**Using Python:**
```bash
# Python 3
python -m http.server 8000

# Python 2
python -m SimpleHTTPServer 8000
```

**Using Node.js:**
```bash
npx http-server -p 8000
```

### Step 2: Open in Browser

Navigate to: `http://localhost:8000`

---

## 🎨 Customization Guide

### Change Colors

Edit the CSS variables in any HTML file:

```css
:root {
  --navy: #0A0E1A;        /* Background */
  --accent: #00F5C8;      /* Primary color */
  --accent2: #0AAFFF;     /* Secondary color */
  --accent3: #7B5CFF;     /* Tertiary color */
  --danger: #FF4B6E;      /* Alert color */
}
```

### Update Content

**Landing Page:**
- Hero text: Line ~140-150
- Features: Line ~250-350
- Pricing: Line ~550-650

**User Dashboard:**
- Privacy score: Line ~180-200
- Documents: Line ~280-400

**Admin Dashboard:**
- Metrics: Line ~140-160
- Alerts: Line ~200-350

**Super Admin:**
- Platform stats: Line ~160-180
- AI config: Line ~250-300

---

## 📱 Test Responsive Design

### Desktop View
- Open in full browser window
- Recommended: 1920x1080 or larger

### Tablet View
- Open browser DevTools (F12)
- Toggle device toolbar
- Select iPad or similar

### Mobile View
- Open browser DevTools (F12)
- Toggle device toolbar
- Select iPhone or similar

---

## 🧪 Interactive Features

### Landing Page
- ✅ Smooth scroll navigation
- ✅ Animated hero section
- ✅ Interactive "How it Works" steps
- ✅ Hover effects on cards

### User Dashboard
- ✅ Document upload modal
- ✅ Share panel with controls
- ✅ Tab filtering
- ✅ Privacy score visualization

### Admin Dashboard
- ✅ Live alert feed
- ✅ Risk user cards
- ✅ Voice bot trigger
- ✅ Security action buttons

### Super Admin
- ✅ AI config sliders
- ✅ Admin management
- ✅ Policy dropdowns
- ✅ System status indicators

---

## 🎓 Demo Scenarios

### Scenario 1: User Journey
1. Start at `index.html` (landing page)
2. Click "Get Started" → Goes to user dashboard
3. Click "Upload Document" → See upload modal
4. Click on a document card → See details
5. Click "Share" → Configure share settings
6. Generate secure link

### Scenario 2: Security Alert
1. Open `admindashboard.html`
2. View "Security Alerts Feed"
3. See high-risk alert for "Ram Sharma"
4. Click "Lock Account" button
5. Click "Voice Call" button
6. See confirmation messages

### Scenario 3: Platform Management
1. Open `superadmin.html`
2. View platform overview stats
3. Adjust AI Guardian sliders
4. Click "Save Changes"
5. Add new admin
6. Configure security policy

---

## 🔍 Troubleshooting

### Issue: Styles not loading
**Solution:** Ensure all files are in the same directory

### Issue: Links not working
**Solution:** Check file names match exactly (case-sensitive)

### Issue: JavaScript not running
**Solution:** Check browser console (F12) for errors

### Issue: Fonts not loading
**Solution:** Check internet connection (fonts load from Google Fonts CDN)

---

## 📊 Feature Checklist

Test all features:

**Landing Page:**
- [ ] Navigation menu works
- [ ] Hero animations play
- [ ] "How it Works" steps are interactive
- [ ] Pricing cards display correctly
- [ ] Footer links present

**User Dashboard:**
- [ ] Sidebar navigation works
- [ ] Privacy score displays
- [ ] Document cards render
- [ ] Upload modal opens
- [ ] Share panel opens
- [ ] Access history table shows

**Admin Dashboard:**
- [ ] Metrics display correctly
- [ ] Alert feed shows items
- [ ] Risk users panel visible
- [ ] Voice bot card present
- [ ] Security controls work
- [ ] Access logs table renders

**Super Admin:**
- [ ] Platform stats display
- [ ] Admin table shows
- [ ] AI config sliders work
- [ ] Document categories list
- [ ] Analytics bars render
- [ ] System status cards show

---

## 🎯 Next Steps

### For Hackathon Demo:
1. ✅ Test all navigation flows
2. ✅ Prepare demo script
3. ✅ Screenshot key features
4. ✅ Practice explaining AI features
5. ✅ Highlight unique features (voice bot, self-destruct)

### For Development:
1. Set up Next.js frontend
2. Build FastAPI backend
3. Configure Supabase database
4. Implement AI models
5. Add authentication
6. Deploy to production

---

## 📚 Additional Resources

### Documentation
- `README.md` - Project overview
- `PROJECT_DOCUMENTATION.md` - Technical details
- `QUICKSTART.md` - This file

### Design Assets
- Color palette in CSS variables
- Icons: Emoji-based (no external dependencies)
- Fonts: Google Fonts (Syne + DM Sans)

### Code Structure
```
datavault-secure/
├── index.html              # Landing page
├── userdashbaord.html      # User dashboard
├── admindashboard.html     # Admin dashboard
├── superadmin.html         # Super admin panel
├── README.md               # Main documentation
├── PROJECT_DOCUMENTATION.md # Technical specs
└── QUICKSTART.md           # This guide
```

---

## 💡 Pro Tips

### For Presentations:
1. Start with landing page to show value prop
2. Demo user dashboard for end-user experience
3. Show admin dashboard for security features
4. Highlight super admin for platform control
5. Emphasize AI features throughout

### For Development:
1. Use browser DevTools to inspect elements
2. Modify CSS variables for quick theme changes
3. Test on multiple screen sizes
4. Check console for any JavaScript errors
5. Use Live Server for auto-reload during edits

### For Hackathons:
1. Focus on unique features (voice bot, self-destruct)
2. Explain AI/ML integration clearly
3. Highlight free tech stack
4. Show scalability potential
5. Demonstrate security features

---

## 🎉 You're Ready!

Your DataVault Secure platform is now ready to demo!

**Quick Links:**
- 🏠 Landing: `index.html`
- 👤 User: `userdashbaord.html`
- 🛡️ Admin: `admindashboard.html`
- 👑 Super Admin: `superadmin.html`

**Need Help?**
- Check `README.md` for overview
- Read `PROJECT_DOCUMENTATION.md` for details
- Review code comments in HTML files

---

**Happy Hacking! 🚀**
