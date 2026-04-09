# 📊 Visual Setup Guide

## 🎯 Complete Setup Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    STEP 1: INSTALL POSTGRESQL                │
│                                                               │
│  Windows: https://www.postgresql.org/download/windows/       │
│  Mac: brew install postgresql                                │
│  Linux: sudo apt install postgresql                          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              STEP 2: UPDATE backend/.env FILE                │
│                                                               │
│  DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@...        │
│                                                               │
│  Default password is usually: postgres                       │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│         STEP 3: RUN DATABASE SETUP SCRIPT                    │
│                                                               │
│  cd backend                                                   │
│  python setup_clean_database.py                              │
│                                                               │
│  Creates:                                                     │
│  ✅ Database: datavault                                      │
│  ✅ Tables: users, documents, shares, access_logs           │
│  ✅ Default users: 3 accounts                               │
│  ✅ Uploads directory                                        │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              STEP 4: START BACKEND SERVER                    │
│                                                               │
│  python app_postgres.py                                      │
│                                                               │
│  Server starts on: http://localhost:8001                     │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│              STEP 5: OPEN FRONTEND & LOGIN                   │
│                                                               │
│  Open: frontend/login_professional.html                      │
│  Login: user@example.com / password                          │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    ✅ READY TO USE!                          │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 File Upload & Storage Flow

```
┌──────────────────────────────────────────────────────────────┐
│                    USER UPLOADS FILE                          │
│                   "my-document.pdf"                           │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                  FRONTEND SENDS TO BACKEND                    │
│         POST /api/documents/upload                            │
│         Authorization: Bearer <token>                         │
│         Content-Type: multipart/form-data                     │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│              BACKEND GENERATES UNIQUE FILENAME                │
│         UUID: 162eed16-c4f4-47c6-9011-7481a6605ad9           │
│         Extension: .pdf                                       │
│         Final: 162eed16-c4f4-47c6-9011-7481a6605ad9.pdf      │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│                  FILE SAVED TO DISK                           │
│         backend/uploads/162eed16-...-7481a6605ad9.pdf        │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│              DATABASE RECORD CREATED                          │
│                                                               │
│  documents table:                                             │
│  ├─ id: "doc-123"                                            │
│  ├─ filename: "162eed16-...-7481a6605ad9.pdf"               │
│  ├─ original_filename: "my-document.pdf"  ← User sees this  │
│  ├─ file_path: "uploads/162eed16-...-7481a6605ad9.pdf"      │
│  ├─ file_size: 245678                                        │
│  ├─ content_type: "application/pdf"                          │
│  └─ user_id: "user-456"                                      │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│              FRONTEND SHOWS DOCUMENT                          │
│         Dashboard displays: "my-document.pdf"                 │
│         With buttons: [View] [Share] [Delete]                │
└──────────────────────────────────────────────────────────────┘
```

---

## 👁️ Document Viewing Flow

```
┌──────────────────────────────────────────────────────────────┐
│              USER CLICKS "VIEW" BUTTON                        │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         FRONTEND: GET DOCUMENT METADATA                       │
│         GET /api/documents/{id}                               │
│         Authorization: Bearer <token>                         │
│                                                               │
│         Response:                                             │
│         {                                                     │
│           "id": "doc-123",                                    │
│           "filename": "162eed16-...-7481a6605ad9.pdf",       │
│           "original_filename": "my-document.pdf",            │
│           "content_type": "application/pdf"                   │
│         }                                                     │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         FRONTEND: GET ACTUAL FILE                             │
│         GET /api/documents/{id}/file                          │
│         Authorization: Bearer <token>  ← IMPORTANT!          │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         BACKEND: VERIFY AUTHENTICATION                        │
│         ✓ Check JWT token valid                              │
│         ✓ Check user owns document                           │
│         ✓ Check file exists on disk                          │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         BACKEND: SERVE FILE                                   │
│         Read: backend/uploads/162eed16-...-7481a6605ad9.pdf  │
│         Return: FileResponse with PDF content                 │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         FRONTEND: CREATE BLOB URL                             │
│         const blob = await response.blob();                   │
│         const blobUrl = URL.createObjectURL(blob);           │
│         → blob:http://localhost/abc-123-def                  │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         FRONTEND: DISPLAY IN MODAL                            │
│                                                               │
│         PDF: <iframe src="blob:http://..."></iframe>         │
│         Image: <img src="blob:http://...">                   │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         BACKEND: LOG ACCESS                                   │
│         INSERT INTO access_logs (                             │
│           user_id, document_id, action='view_file'           │
│         )                                                     │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│              ✅ USER SEES DOCUMENT!                           │
└──────────────────────────────────────────────────────────────┘
```

---

## 🗄️ Database Structure

```
┌─────────────────────────────────────────────────────────────┐
│                    POSTGRESQL DATABASE                        │
│                      "datavault"                              │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ↓                     ↓                     ↓
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│    users     │    │  documents   │    │    shares    │
├──────────────┤    ├──────────────┤    ├──────────────┤
│ id (PK)      │←───│ user_id (FK) │    │ id (PK)      │
│ email        │    │ id (PK)      │←───│ document_id  │
│ password_hash│    │ filename     │    │ user_id (FK) │
│ full_name    │    │ original_name│    │ share_token  │
│ role         │    │ file_path    │    │ expires_at   │
│ is_active    │    │ file_size    │    │ access_count │
│ created_at   │    │ content_type │    │ status       │
└──────────────┘    │ is_shared    │    └──────────────┘
                    │ is_verified  │
                    │ created_at   │
                    └──────────────┘
                            │
                            ↓
                    ┌──────────────┐
                    │ access_logs  │
                    ├──────────────┤
                    │ id (PK)      │
                    │ user_id (FK) │
                    │ document_id  │
                    │ action       │
                    │ timestamp    │
                    │ ip_address   │
                    │ device       │
                    │ risk_level   │
                    └──────────────┘
```

---

## 🔐 Authentication Flow

```
┌──────────────────────────────────────────────────────────────┐
│              USER ENTERS CREDENTIALS                          │
│         Email: user@example.com                               │
│         Password: password                                    │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         FRONTEND: POST /api/auth/login                        │
│         { "email": "...", "password": "..." }                │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         BACKEND: VERIFY CREDENTIALS                           │
│         1. Find user by email                                 │
│         2. Hash provided password                             │
│         3. Compare with stored password_hash                  │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         BACKEND: GENERATE JWT TOKEN                           │
│         Token contains:                                       │
│         - User email                                          │
│         - Expiration time (24 hours)                          │
│         - Signature (SECRET_KEY)                              │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         BACKEND: RETURN TOKEN                                 │
│         {                                                     │
│           "access_token": "eyJhbGci...",                     │
│           "token_type": "bearer",                            │
│           "user": { "email": "...", "role": "..." }          │
│         }                                                     │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         FRONTEND: STORE TOKEN                                 │
│         localStorage.setItem('access_token', token)          │
└──────────────────────────────────────────────────────────────┘
                              ↓
┌──────────────────────────────────────────────────────────────┐
│         FRONTEND: USE TOKEN FOR ALL REQUESTS                  │
│         headers: {                                            │
│           'Authorization': 'Bearer eyJhbGci...'              │
│         }                                                     │
└──────────────────────────────────────────────────────────────┘
```

---

## 📂 Directory Structure

```
doc-final/
│
├── backend/
│   ├── .env                    ← UPDATE YOUR PASSWORD HERE! ⭐
│   ├── .env.example            ← Configuration template
│   ├── app_postgres.py         ← Main backend server
│   ├── setup_clean_database.py ← Run this first! ⭐
│   ├── migrate_access_logs.py
│   ├── requirements.txt
│   │
│   └── uploads/                ← Files stored here ⭐
│       ├── 162eed16-c4f4-47c6-9011-7481a6605ad9.pdf
│       ├── 242c5fb9-e117-42f8-b80d-9d4906776718.pdf
│       └── 44193c3b-d53b-4e3f-8b6e-1245f97fd391.png
│
├── frontend/
│   ├── login_professional.html ← Start here! ⭐
│   ├── dashboard.html
│   ├── my-documents.html
│   ├── admin.html
│   ├── superadmin.html
│   ├── config.js
│   │
│   └── assets/
│       └── js/
│           ├── api.js
│           ├── dashboard.js
│           └── auth.js
│
├── START_HERE.md               ← Read this first! ⭐
├── COMPLETE_SETUP_README.md    ← Full documentation
├── SETUP_COMPLETE_SUMMARY.md   ← Detailed summary
├── QUICK_SETUP.bat             ← Windows quick setup
├── test_login.py               ← Test backend
└── test_frontend_connection.html ← Test frontend
```

---

## ✅ Verification Checklist

```
□ PostgreSQL installed and running
    └─ Windows: Services → postgresql-x64-XX
    └─ Mac: brew services list
    └─ Linux: sudo systemctl status postgresql

□ Database configured in backend/.env
    └─ DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/datavault

□ Database setup completed
    └─ Run: python backend/setup_clean_database.py
    └─ Check: psql -U postgres -d datavault -c "\dt"

□ Backend server running
    └─ Run: python backend/app_postgres.py
    └─ Check: curl http://localhost:8001/health

□ Frontend accessible
    └─ Open: frontend/login_professional.html
    └─ Login: user@example.com / password

□ File upload working
    └─ Upload a PDF file
    └─ Check: ls backend/uploads/
    └─ Check: psql -U postgres -d datavault -c "SELECT * FROM documents;"

□ File viewing working
    └─ Click "View" on uploaded document
    └─ PDF should display in modal
    └─ Check browser console for errors (F12)
```

---

## 🎯 Quick Commands Reference

```bash
# Setup database
cd backend
python setup_clean_database.py

# Start backend
python app_postgres.py

# Test backend
python test_login.py
curl http://localhost:8001/health

# Check database
psql -U postgres -d datavault
\dt                          # List tables
SELECT * FROM users;         # View users
SELECT * FROM documents;     # View documents
\q                           # Quit

# Check uploaded files
ls backend/uploads/          # Mac/Linux
dir backend\uploads\         # Windows

# Stop backend
Ctrl+C

# Restart PostgreSQL
# Windows: Services → postgresql → Restart
# Mac: brew services restart postgresql
# Linux: sudo systemctl restart postgresql
```

---

## 🆘 Quick Troubleshooting

| Problem | Solution |
|---------|----------|
| "Database connection failed" | Check PostgreSQL is running |
| "Cannot login" | Check backend is running on port 8001 |
| "Files not visible" | Clear browser cache (Ctrl+Shift+Delete) |
| "Port 8001 in use" | Stop existing process: `netstat -ano \| findstr :8001` |
| "Permission denied" | Check PostgreSQL user has correct permissions |

---

**🎉 You're ready to use DataVault!**

Files are stored clearly in `backend/uploads/` and visible in the application with proper authentication!
