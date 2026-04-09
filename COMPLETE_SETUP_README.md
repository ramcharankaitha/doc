# DataVault Secure - Complete Setup Guide

## 🚀 Quick Start (3 Steps)

### Step 1: Install PostgreSQL
- **Windows**: Download from https://www.postgresql.org/download/windows/
- **Mac**: `brew install postgresql && brew services start postgresql`
- **Linux**: `sudo apt install postgresql && sudo systemctl start postgresql`

### Step 2: Configure Database
1. Open `backend/.env` file
2. Update DATABASE_URL with your PostgreSQL password:
   ```env
   DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/datavault
   ```
   (Default password is usually `postgres`)

### Step 3: Run Setup
```bash
# Windows
QUICK_SETUP.bat

# Mac/Linux
cd backend
python setup_clean_database.py
python app_postgres.py
```

Then open `frontend/login_professional.html` in your browser!

---

## 📋 Detailed Setup Instructions

### Prerequisites

1. **Python 3.8+**
   ```bash
   python --version
   ```

2. **PostgreSQL 12+**
   ```bash
   psql --version
   ```

3. **Install Python Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

### Database Configuration

#### Option 1: Default Setup (Recommended)
If you installed PostgreSQL with default settings:
- Username: `postgres`
- Password: `postgres`
- Host: `localhost`
- Port: `5432`

Your `.env` file should have:
```env
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/datavault
```

#### Option 2: Custom Setup
If you have different PostgreSQL credentials:

1. Open `backend/.env`
2. Update the DATABASE_URL:
   ```env
   DATABASE_URL=postgresql://YOUR_USERNAME:YOUR_PASSWORD@localhost:5432/datavault
   ```

#### Option 3: Remote Database
If PostgreSQL is on a different server:
```env
DATABASE_URL=postgresql://postgres:password@192.168.1.100:5432/datavault
```

### Running the Setup

#### Automatic Setup (Windows)
```bash
QUICK_SETUP.bat
```

#### Manual Setup (All Platforms)

1. **Create Clean Database**
   ```bash
   cd backend
   python setup_clean_database.py
   ```
   
   This will:
   - Create `datavault` database
   - Create all tables (users, documents, shares, access_logs)
   - Create default admin users
   - Set up uploads directory

2. **Start Backend Server**
   ```bash
   python app_postgres.py
   ```
   
   Server will start on: http://localhost:8001

3. **Open Frontend**
   - Open `frontend/login_professional.html` in your browser
   - Or use any web server to serve the frontend files

### Default Login Credentials

| Role | Email | Password |
|------|-------|----------|
| Super Admin | superadmin@datavault.com | SuperAdmin2024! |
| Admin | admin@datavault.com | Admin2024! |
| User | user@example.com | password |

---

## 📁 File Upload and Viewing

### How It Works

1. **Upload a Document**
   - Login to the application
   - Click "Upload Document" button
   - Select a PDF or image file
   - File is uploaded and stored

2. **File Storage**
   - Files are stored in `backend/uploads/` directory
   - Each file gets a unique UUID filename
   - Original filename is preserved in database

3. **View Documents**
   - Click "View" button on any document
   - PDF files open in modal viewer
   - Images display directly
   - All views require authentication

### File Storage Structure

```
backend/
└── uploads/
    ├── 162eed16-c4f4-47c6-9011-7481a6605ad9.pdf  ← Stored file
    ├── 242c5fb9-e117-42f8-b80d-9d4906776718.pdf
    └── 44193c3b-d53b-4e3f-8b6e-1245f97fd391.png

Database Record:
{
  "id": "doc-123",
  "filename": "162eed16-c4f4-47c6-9011-7481a6605ad9.pdf",
  "original_filename": "my-document.pdf",  ← Original name shown to user
  "file_path": "uploads/162eed16-c4f4-47c6-9011-7481a6605ad9.pdf",
  "file_size": 245678,
  "content_type": "application/pdf"
}
```

### Supported File Types

- **PDF Documents**: `.pdf`
- **Images**: `.jpg`, `.jpeg`, `.png`
- **Max Size**: 10MB per file

---

## 🗄️ Database Schema

### Tables

#### users
Stores user accounts and authentication
- `id`, `email`, `password_hash`, `full_name`, `role`, `is_active`, `privacy_score`

#### documents
Stores document metadata and file information
- `id`, `user_id`, `filename`, `original_filename`, `file_path`, `file_size`, `content_type`, `category`, `privacy_score`, `is_shared`, `is_verified`, `blockchain_hash`

#### shares
Stores document sharing links and permissions
- `id`, `document_id`, `user_id`, `share_token`, `expires_at`, `access_count`, `max_access`, `status`

#### access_logs
Stores all access and activity logs
- `id`, `user_id`, `document_id`, `action`, `timestamp`, `ip_address`, `device`, `user_agent`, `location`, `risk_level`, `status`

### View Database Contents

```bash
# Connect to database
psql -U postgres -d datavault

# View all users
SELECT email, role, created_at FROM users;

# View all documents
SELECT original_filename, file_size, created_at FROM documents;

# View recent activity
SELECT action, timestamp FROM access_logs ORDER BY timestamp DESC LIMIT 10;
```

---

## 🔧 Troubleshooting

### Issue: "Database connection failed"

**Cause**: PostgreSQL not running or wrong credentials

**Solution**:
1. Check PostgreSQL is running:
   - Windows: Services → postgresql-x64-XX
   - Mac: `brew services list`
   - Linux: `sudo systemctl status postgresql`

2. Verify credentials in `backend/.env`

3. Test connection:
   ```bash
   psql -U postgres -h localhost -p 5432
   ```

### Issue: "Cannot login to application"

**Cause**: Backend not running or wrong URL

**Solution**:
1. Check backend is running on port 8001:
   ```bash
   curl http://localhost:8001/health
   ```

2. Check browser console for errors (F12)

3. Clear browser cache (Ctrl+Shift+Delete)

### Issue: "Files not visible after upload"

**Cause**: Database or file system issue

**Solution**:
1. Check `backend/uploads/` directory exists
2. Verify file was saved:
   ```bash
   ls backend/uploads/
   ```
3. Check database record:
   ```sql
   SELECT * FROM documents;
   ```
4. Clear browser cache and refresh

### Issue: "Cannot view PDF files"

**Cause**: Authentication or file access issue

**Solution**:
1. Check file exists in `backend/uploads/`
2. Verify you're logged in (check localStorage for access_token)
3. Check browser console for errors
4. Test with `test_pdf_viewer.html`

### Issue: "Port 8001 already in use"

**Cause**: Another process using the port

**Solution**:
```bash
# Windows
netstat -ano | findstr :8001
taskkill /PID <PID> /F

# Mac/Linux
lsof -i :8001
kill -9 <PID>
```

---

## 📊 Testing the Setup

### Test 1: Backend Health
```bash
curl http://localhost:8001/health
```
Expected: `{"status":"healthy","database":"PostgreSQL","users":3,"documents":0}`

### Test 2: Login API
```bash
python test_login.py
```
Expected: `✅ Login successful!`

### Test 3: Frontend Connection
1. Open `test_frontend_connection.html` in browser
2. Click "Test Backend Connection"
3. Click "Test Login"
Both should show ✅ success

### Test 4: Full Application
1. Open `frontend/login_professional.html`
2. Login with `user@example.com` / `password`
3. Upload a PDF file
4. Click "View" on the uploaded document
5. Document should display in modal viewer

---

## 🔒 Security Best Practices

### For Development
- ✅ Use default credentials (already configured)
- ✅ CORS set to allow all origins
- ✅ Debug mode enabled

### For Production
1. **Change All Passwords**
   ```env
   SECRET_KEY=use-long-random-string-here
   JWT_SECRET_KEY=use-different-long-random-string
   DATABASE_URL=postgresql://postgres:STRONG_PASSWORD@localhost:5432/datavault
   ```

2. **Update CORS**
   ```env
   CORS_ORIGINS=https://yourdomain.com
   ```

3. **Enable SSL**
   - Use HTTPS for frontend
   - Enable SSL for PostgreSQL connection

4. **Set Up Backups**
   ```bash
   # Daily backup
   pg_dump -U postgres datavault > backup_$(date +%Y%m%d).sql
   ```

5. **Monitor Logs**
   - Check access_logs table regularly
   - Set up alerts for suspicious activity

---

## 📚 Additional Resources

### Documentation Files
- `CLEAN_DATABASE_SETUP_GUIDE.md` - Detailed database setup
- `BACKEND_LOGIN_FIX_COMPLETE.md` - Authentication details
- `PDF_VIEWER_AUTHENTICATION_FIX.md` - File viewing details
- `POSTGRESQL_SETUP.md` - PostgreSQL configuration

### Test Files
- `test_login.py` - Test backend authentication
- `test_frontend_connection.html` - Test frontend connectivity
- `test_pdf_viewer.html` - Test PDF viewer functionality

### Configuration Files
- `backend/.env` - Environment configuration
- `backend/.env.example` - Configuration template
- `frontend/config.js` - Frontend API configuration

---

## 🎯 What You Get

### ✅ Clean Database
- Fresh PostgreSQL database
- All tables created with proper schema
- Indexes for performance
- Foreign key constraints

### ✅ Default Users
- 3 pre-configured accounts (superadmin, admin, user)
- Ready to login immediately
- Different permission levels

### ✅ File Management
- Upload PDF and image files
- Files stored securely on disk
- Metadata in database
- Unique filenames prevent conflicts

### ✅ Document Viewing
- PDF viewer with authentication
- Image viewer
- Download option for other files
- Access logging

### ✅ Security
- JWT authentication
- Password hashing
- CORS protection
- Access control
- Activity logging

---

## 🚀 Next Steps

1. **Customize the Application**
   - Update branding in frontend files
   - Modify user roles and permissions
   - Add custom document categories

2. **Add Features**
   - Email notifications
   - Two-factor authentication
   - Document versioning
   - Advanced search

3. **Deploy to Production**
   - Set up production database
   - Configure SSL certificates
   - Set up domain and hosting
   - Enable monitoring and backups

---

**Status**: ✅ Ready for Use
**Database**: Clean PostgreSQL setup
**Files**: Properly stored and viewable
**Authentication**: Fully functional
**Documentation**: Complete

**Need Help?** Check the troubleshooting section or review the detailed guides in the documentation files.
