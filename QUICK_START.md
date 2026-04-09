# 🚀 Quick Start Guide

## ✅ Everything is Ready!

Your DataVault application is now fully configured with PostgreSQL and persistent storage.

## 🎯 Current Status

- ✅ Backend running on http://localhost:8001
- ✅ Frontend running on http://localhost:3000
- ✅ PostgreSQL database connected
- ✅ 3 users ready to use
- ✅ Document upload working
- ✅ All data persists permanently

## 🔐 Login Now

### Option 1: Test User (Recommended for Testing)
```
URL: http://localhost:3000/login.html

Email: user@example.com
Password: password
```

### Option 2: Admin
```
Email: admin@datavault.com
Password: Admin2024!
```

### Option 3: Super Admin
```
Email: superadmin@datavault.com
Password: SuperAdmin2024!
```

## 📤 Upload Documents

1. **Login** at http://localhost:3000/login.html
2. **Click** "+ Upload Document" button
3. **Select** JPG, PNG, or PDF file (max 10MB)
4. **Done!** Document uploads and saves permanently

## ✨ Key Features

### What Works Now
- ✅ User login (persistent accounts)
- ✅ Document upload (saves to PostgreSQL)
- ✅ Document viewing (from database)
- ✅ Document sharing
- ✅ Privacy score tracking
- ✅ Access history
- ✅ Admin dashboard
- ✅ **No more data loss!**

### Data Persistence
- ✅ Users never disappear
- ✅ Documents always available
- ✅ Survives server restarts
- ✅ Production-ready storage

## 🔄 Restart Servers (If Needed)

### Stop Servers
Press `Ctrl+C` in both terminal windows

### Start Backend
```bash
cd backend
python app.py
```

### Start Frontend
```bash
cd frontend
python app.py
```

## 🧪 Test Everything

### Quick Test
1. Go to http://localhost:8001/health
2. Should see:
   ```json
   {
     "status": "healthy",
     "database": "PostgreSQL",
     "users": 3,
     "documents": X
   }
   ```

### Full Test
1. Login at http://localhost:3000/login.html
2. Upload a document
3. See it in your dashboard
4. Restart backend server
5. Login again
6. **Document is still there!** ✅

## 📊 Check Database

### View Users
```bash
psql -U postgres -d datavault
SELECT email, role FROM users;
\q
```

### View Documents
```bash
psql -U postgres -d datavault
SELECT original_filename, user_id FROM documents;
\q
```

## 🎯 Common Tasks

### Upload Document via API
```bash
# 1. Login
curl -X POST http://localhost:8001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password"}'

# 2. Upload (replace YOUR_TOKEN)
curl -X POST http://localhost:8001/api/documents/upload \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@document.pdf"
```

### Get All Documents
```bash
curl -X GET http://localhost:8001/api/documents/ \
  -H "Authorization: Bearer YOUR_TOKEN"
```

## 🐛 Troubleshooting

### Backend Not Starting
```bash
# Check PostgreSQL is running
Get-Service -Name "*postgresql*"

# If not running, start it
# Then restart backend
cd backend
python app.py
```

### Frontend Not Loading
```bash
# Restart frontend
cd frontend
python app.py
```

### Can't Login
- Use exact credentials above
- Check backend is running: http://localhost:8001/health
- Clear browser cache and try again

### Documents Not Showing
- Check backend logs for errors
- Verify upload was successful (check response)
- Refresh the page

## 📚 More Information

- **Complete Setup**: See `POSTGRESQL_SETUP.md`
- **Upload Guide**: See `UPLOAD_GUIDE.md`
- **Full Summary**: See `FINAL_SOLUTION_SUMMARY.md`

## 🎉 You're All Set!

Your application is ready to use with:
- ✅ Persistent PostgreSQL database
- ✅ Working document upload
- ✅ No data loss
- ✅ Production-ready

**Start using it now at**: http://localhost:3000/login.html

---

**Need Help?**
1. Check http://localhost:8001/health
2. Review backend terminal for errors
3. See troubleshooting section above
4. Check documentation files
