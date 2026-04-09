# 🚀 START HERE - DataVault Secure Setup

## Quick Setup (5 Minutes)

### 1️⃣ Install PostgreSQL
**Windows**: https://www.postgresql.org/download/windows/  
**Mac**: `brew install postgresql && brew services start postgresql`  
**Linux**: `sudo apt install postgresql && sudo systemctl start postgresql`

### 2️⃣ Configure Database Password
Open `backend/.env` and update this line with your PostgreSQL password:
```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/datavault
```
(If you used default installation, password is usually `postgres`)

### 3️⃣ Run Setup Script
```bash
cd backend
python setup_clean_database.py
```

### 4️⃣ Start Backend
```bash
python app_postgres.py
```

### 5️⃣ Open Frontend
Open `frontend/login_professional.html` in your browser

### 6️⃣ Login
**Email**: user@example.com  
**Password**: password

---

## ✅ What This Setup Does

1. **Creates Clean Database**
   - Fresh PostgreSQL database named `datavault`
   - All tables: users, documents, shares, access_logs
   - Proper indexes and foreign keys

2. **Creates Default Users**
   - Super Admin: superadmin@datavault.com / SuperAdmin2024!
   - Admin: admin@datavault.com / Admin2024!
   - User: user@example.com / password

3. **Sets Up File Storage**
   - Creates `backend/uploads/` directory
   - Configures file upload handling
   - Max file size: 10MB

4. **Enables Features**
   - ✅ User authentication (JWT)
   - ✅ Document upload (PDF, images)
   - ✅ Document viewing (with authentication)
   - ✅ Document sharing (secure links)
   - ✅ Access logging (audit trail)
   - ✅ Admin panels (user management)

---

## 📁 How Files Work

### Upload Process
1. User uploads file → Frontend sends to backend
2. Backend generates unique filename (UUID)
3. File saved to `backend/uploads/`
4. Database record created with metadata

### File Storage
```
backend/uploads/
├── 162eed16-c4f4-47c6-9011-7481a6605ad9.pdf  ← Your uploaded file
├── 242c5fb9-e117-42f8-b80d-9d4906776718.pdf
└── 44193c3b-d53b-4e3f-8b6e-1245f97fd391.png
```

### Viewing Files
1. Click "View" button → Frontend requests file
2. Backend verifies authentication
3. Backend serves file from disk
4. Frontend displays in modal (PDF/image viewer)

**All files are visible and viewable after upload!**

---

## 🔍 Verify Setup

### Test 1: Check Backend
```bash
curl http://localhost:8001/health
```
Should return: `{"status":"healthy","database":"PostgreSQL"}`

### Test 2: Check Database
```bash
psql -U postgres -d datavault -c "SELECT COUNT(*) FROM users;"
```
Should return: `3` (default users)

### Test 3: Test Login
```bash
python test_login.py
```
Should show: `✅ Login successful!`

### Test 4: Upload and View
1. Login to application
2. Upload a PDF file
3. Click "View" button
4. PDF should display in modal

---

## 🆘 Common Issues

### "Database connection failed"
→ PostgreSQL not running. Start it:
- Windows: Services → postgresql
- Mac: `brew services start postgresql`
- Linux: `sudo systemctl start postgresql`

### "Cannot login"
→ Backend not running. Start it:
```bash
cd backend
python app_postgres.py
```

### "Files not visible"
→ Clear browser cache: Ctrl+Shift+Delete

### "Port 8001 in use"
→ Stop existing process:
```bash
# Windows
netstat -ano | findstr :8001
taskkill /PID <PID> /F
```

---

## 📚 Documentation

- **COMPLETE_SETUP_README.md** - Full setup guide
- **CLEAN_DATABASE_SETUP_GUIDE.md** - Database details
- **backend/.env.example** - Configuration template
- **BACKEND_LOGIN_FIX_COMPLETE.md** - Authentication info

---

## 🎯 What's Configured

### Backend (Port 8001)
- ✅ PostgreSQL database connection
- ✅ JWT authentication
- ✅ File upload/download
- ✅ CORS enabled (all origins)
- ✅ API documentation: http://localhost:8001/api/docs

### Frontend
- ✅ Login page: `frontend/login_professional.html`
- ✅ Dashboard: `frontend/dashboard.html`
- ✅ My Documents: `frontend/my-documents.html`
- ✅ Admin Panel: `frontend/admin.html`
- ✅ Super Admin: `frontend/superadmin.html`

### Database
- ✅ Database: `datavault`
- ✅ Tables: users, documents, shares, access_logs
- ✅ Default users: 3 accounts
- ✅ Indexes: Optimized for performance

### File Storage
- ✅ Directory: `backend/uploads/`
- ✅ Supported: PDF, JPG, PNG
- ✅ Max size: 10MB
- ✅ Unique filenames: UUID-based

---

## 🚀 Ready to Use!

Your application is now fully configured with:
- Clean PostgreSQL database
- Default admin accounts
- File upload and viewing
- Secure authentication
- Complete documentation

**Start the backend and login to begin!**

```bash
cd backend
python app_postgres.py
```

Then open `frontend/login_professional.html` and login with:
- **Email**: user@example.com
- **Password**: password

---

**Need Help?** Check the troubleshooting section above or review the detailed documentation files.
