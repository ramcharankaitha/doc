# Clean PostgreSQL Database Setup Guide

## Prerequisites

### 1. Install PostgreSQL

**Windows:**
- Download from: https://www.postgresql.org/download/windows/
- Run installer and remember your password for the `postgres` user
- Default port: 5432

**Mac:**
```bash
brew install postgresql
brew services start postgresql
```

**Linux (Ubuntu/Debian):**
```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql
```

### 2. Verify PostgreSQL is Running

**Windows:**
- Open Services (Win+R, type `services.msc`)
- Look for "postgresql-x64-XX" service
- Status should be "Running"

**Mac/Linux:**
```bash
psql --version
sudo systemctl status postgresql  # Linux
brew services list  # Mac
```

### 3. Install Python Dependencies

```bash
cd backend
pip install -r requirements.txt
```

Required packages:
- psycopg2-binary (PostgreSQL adapter)
- sqlalchemy (ORM)
- fastapi
- uvicorn
- python-jose[cryptography]
- passlib

## Setup Steps

### Step 1: Configure Database Connection

Edit `backend/.env` file:

```env
# Database Configuration
# Update these values if your PostgreSQL setup is different
DATABASE_URL=postgresql://postgres:postgres@localhost:5432/datavault

# If you have a different PostgreSQL password:
# DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/datavault
```

**Common PostgreSQL Configurations:**

| Setup | DATABASE_URL |
|-------|-------------|
| Default (password: postgres) | `postgresql://postgres:postgres@localhost:5432/datavault` |
| Custom password | `postgresql://postgres:YOUR_PASSWORD@localhost:5432/datavault` |
| Different port | `postgresql://postgres:postgres@localhost:5433/datavault` |
| Remote server | `postgresql://postgres:postgres@192.168.1.100:5432/datavault` |

### Step 2: Run Clean Database Setup

```bash
cd backend
python setup_clean_database.py
```

This script will:
1. ✅ Create the `datavault` database (or drop and recreate if exists)
2. ✅ Create all required tables (users, documents, shares, access_logs)
3. ✅ Create indexes for performance
4. ✅ Create default admin users
5. ✅ Create uploads directory
6. ✅ Verify the setup

**Expected Output:**
```
============================================================
🗄️  PostgreSQL Database Setup
============================================================
📦 Creating database 'datavault'...
✅ Database 'datavault' created successfully

📋 Creating database tables...
✅ All tables created successfully

👥 Creating default users...
  ✅ Created superadmin: superadmin@datavault.com
  ✅ Created admin: admin@datavault.com
  ✅ Created user: user@example.com
✅ Default users created successfully

🔍 Verifying database setup...
  📋 Tables created: 4
     - access_logs
     - documents
     - shares
     - users
  👥 Users: 3
  📄 Documents: 0
✅ Database verification complete

📁 Setting up uploads directory...
✅ Created 'uploads' directory

============================================================
✅ DATABASE SETUP COMPLETE!
============================================================
```

### Step 3: Start the Backend Server

```bash
cd backend
python app_postgres.py
```

**Expected Output:**
```
============================================================
🚀 DataVault Secure - Backend with PostgreSQL
============================================================
📍 Server: http://localhost:8001
📚 API Docs: http://localhost:8001/api/docs
🗄️  Database: PostgreSQL

👑 Administrator Accounts:
   Super Admin: superadmin@datavault.com / SuperAdmin2024!
   Admin: admin@datavault.com / Admin2024!
   User: user@example.com / password

⏹️  Press Ctrl+C to stop
============================================================
INFO:     Uvicorn running on http://0.0.0.0:8001 (Press CTRL+C to quit)
```

### Step 4: Test the Setup

**Option 1: Use Test Script**
```bash
python test_login.py
```

**Option 2: Open Frontend**
1. Open `frontend/login_professional.html` in your browser
2. Login with: `user@example.com` / `password`
3. Upload a document
4. View the document (should display correctly)

## Database Schema

### Tables Created:

#### 1. users
- `id` (VARCHAR, PRIMARY KEY)
- `email` (VARCHAR, UNIQUE)
- `password_hash` (VARCHAR)
- `full_name` (VARCHAR)
- `role` (VARCHAR) - 'user', 'admin', 'superadmin'
- `is_active` (BOOLEAN)
- `privacy_score` (INTEGER)
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)

#### 2. documents
- `id` (VARCHAR, PRIMARY KEY)
- `user_id` (VARCHAR, FOREIGN KEY)
- `filename` (VARCHAR) - Stored filename
- `original_filename` (VARCHAR) - Original upload name
- `file_path` (VARCHAR) - Path to file on disk
- `file_size` (INTEGER) - Size in bytes
- `content_type` (VARCHAR) - MIME type
- `category` (VARCHAR) - Document category
- `privacy_score` (INTEGER)
- `is_shared` (BOOLEAN)
- `is_verified` (BOOLEAN)
- `blockchain_hash` (VARCHAR)
- `created_at` (TIMESTAMP)
- `updated_at` (TIMESTAMP)

#### 3. shares
- `id` (VARCHAR, PRIMARY KEY)
- `document_id` (VARCHAR, FOREIGN KEY)
- `user_id` (VARCHAR, FOREIGN KEY)
- `share_token` (VARCHAR, UNIQUE)
- `document_name` (VARCHAR)
- `created_at` (TIMESTAMP)
- `expires_at` (TIMESTAMP)
- `access_count` (INTEGER)
- `max_access` (INTEGER)
- `status` (VARCHAR)

#### 4. access_logs
- `id` (VARCHAR, PRIMARY KEY)
- `user_id` (VARCHAR, FOREIGN KEY)
- `document_id` (VARCHAR)
- `action` (VARCHAR)
- `timestamp` (TIMESTAMP)
- `ip_address` (VARCHAR)
- `device` (VARCHAR)
- `user_agent` (VARCHAR)
- `location` (VARCHAR)
- `risk_level` (VARCHAR)
- `status` (VARCHAR)

## Default User Accounts

| Role | Email | Password | Access Level |
|------|-------|----------|--------------|
| Super Admin | superadmin@datavault.com | SuperAdmin2024! | Full system access |
| Admin | admin@datavault.com | Admin2024! | User management |
| User | user@example.com | password | Document management |

## File Upload and Viewing

### How Files Are Stored:

1. **Upload Process:**
   - User uploads file through frontend
   - Backend generates unique filename (UUID + extension)
   - File saved to `backend/uploads/` directory
   - Database record created with file metadata

2. **File Storage Structure:**
   ```
   backend/
   └── uploads/
       ├── 162eed16-c4f4-47c6-9011-7481a6605ad9.pdf
       ├── 242c5fb9-e117-42f8-b80d-9d4906776718.pdf
       └── 44193c3b-d53b-4e3f-8b6e-1245f97fd391.png
   ```

3. **Database Record:**
   ```json
   {
     "id": "doc-uuid",
     "filename": "162eed16-c4f4-47c6-9011-7481a6605ad9.pdf",
     "original_filename": "my-document.pdf",
     "file_path": "uploads/162eed16-c4f4-47c6-9011-7481a6605ad9.pdf",
     "file_size": 245678,
     "content_type": "application/pdf"
   }
   ```

### Viewing Files:

1. **Frontend Request:**
   - User clicks "View" button
   - Frontend fetches document metadata
   - Frontend requests file with authentication

2. **Backend Response:**
   - Verifies JWT token
   - Checks user owns document
   - Serves file from disk
   - Logs access in access_logs table

3. **Display:**
   - PDF: Rendered in iframe
   - Images: Displayed in img tag
   - Other: Download option

## Troubleshooting

### Issue: "Database connection failed"

**Solution:**
1. Check PostgreSQL is running
2. Verify credentials in `.env` file
3. Test connection:
   ```bash
   psql -U postgres -h localhost -p 5432
   ```

### Issue: "Database 'datavault' already exists"

**Solution:**
Run setup script and choose "yes" to drop and recreate:
```bash
python setup_clean_database.py
# When prompted: yes
```

### Issue: "Permission denied for database"

**Solution:**
Grant permissions to postgres user:
```sql
GRANT ALL PRIVILEGES ON DATABASE datavault TO postgres;
```

### Issue: "Files not visible after upload"

**Solution:**
1. Check `backend/uploads/` directory exists
2. Verify file was saved (check directory)
3. Check database record was created:
   ```sql
   SELECT * FROM documents;
   ```
4. Clear browser cache (Ctrl+F5)

### Issue: "Cannot view PDF files"

**Solution:**
1. Check file exists in `backend/uploads/`
2. Verify authentication token is valid
3. Check browser console for errors
4. Test with `test_pdf_viewer.html`

## Maintenance

### View Database Contents:

```bash
# Connect to database
psql -U postgres -d datavault

# View users
SELECT id, email, role, created_at FROM users;

# View documents
SELECT id, original_filename, file_size, created_at FROM documents;

# View access logs
SELECT action, timestamp, status FROM access_logs ORDER BY timestamp DESC LIMIT 10;
```

### Backup Database:

```bash
pg_dump -U postgres datavault > datavault_backup.sql
```

### Restore Database:

```bash
psql -U postgres datavault < datavault_backup.sql
```

### Clean Old Files:

```bash
# Remove uploaded files
rm -rf backend/uploads/*

# Clear database records
psql -U postgres -d datavault -c "TRUNCATE documents CASCADE;"
```

## Production Considerations

1. **Change Default Passwords:**
   - Update `.env` SECRET_KEY
   - Change default user passwords
   - Use strong PostgreSQL password

2. **Security:**
   - Enable SSL for PostgreSQL
   - Use environment variables for sensitive data
   - Implement rate limiting
   - Add file virus scanning

3. **Performance:**
   - Add database connection pooling
   - Implement file caching
   - Use CDN for static files
   - Add database indexes

4. **Monitoring:**
   - Set up database backups
   - Monitor disk space for uploads
   - Log all access attempts
   - Set up alerts for errors

---

**Status**: Ready for use
**Database**: Clean PostgreSQL setup
**Files**: Properly stored and viewable
**Authentication**: Fully functional
