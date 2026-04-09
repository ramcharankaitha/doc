# PostgreSQL Setup Guide

## 🎯 Why PostgreSQL?

Your application now uses PostgreSQL for persistent data storage. This means:
- ✅ Users are saved permanently (no more disappearing users)
- ✅ Documents are stored in database (persistent across restarts)
- ✅ All data survives server restarts
- ✅ Production-ready database solution

## 📋 Prerequisites

### Install PostgreSQL

#### Windows
1. Download PostgreSQL from: https://www.postgresql.org/download/windows/
2. Run the installer
3. During installation:
   - Set password for postgres user: `postgres`
   - Port: `5432` (default)
   - Remember these credentials!

#### Mac
```bash
brew install postgresql
brew services start postgresql
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib
sudo systemctl start postgresql
```

## 🚀 Quick Setup

### Option 1: Automatic Setup (Recommended)

```bash
cd backend
python setup_postgres.py
```

This will:
- Create the `datavault` database
- Test the connection
- Verify everything is working

### Option 2: Manual Setup

1. **Start PostgreSQL**
   - Windows: PostgreSQL should start automatically
   - Mac: `brew services start postgresql`
   - Linux: `sudo systemctl start postgresql`

2. **Create Database**
   ```bash
   psql -U postgres
   CREATE DATABASE datavault;
   \q
   ```

3. **Update Configuration**
   Edit `backend/.env`:
   ```
   DATABASE_URL=postgresql://postgres:postgres@localhost:5432/datavault
   ```

4. **Start Backend**
   ```bash
   cd backend
   python app.py
   ```

The application will automatically create all tables on first startup!

## 🔧 Configuration

### Database Connection String Format
```
DATABASE_URL=postgresql://username:password@host:port/database
```

### Default Configuration
```
Username: postgres
Password: postgres
Host: localhost
Port: 5432
Database: datavault
```

### Update Your Configuration
Edit `backend/.env` if your PostgreSQL uses different credentials:
```env
DATABASE_URL=postgresql://YOUR_USER:YOUR_PASSWORD@localhost:5432/datavault
```

## ✅ Verify Setup

### 1. Check PostgreSQL is Running

**Windows:**
- Open Services (services.msc)
- Look for "postgresql-x64-XX" service
- Status should be "Running"

**Mac:**
```bash
brew services list | grep postgresql
```

**Linux:**
```bash
sudo systemctl status postgresql
```

### 2. Test Database Connection

```bash
cd backend
python setup_postgres.py
```

You should see:
```
✅ Database 'datavault' created successfully
✅ Connected to PostgreSQL
✅ PostgreSQL setup complete!
```

### 3. Start the Application

```bash
cd backend
python app.py
```

You should see:
```
🚀 DataVault Secure - Backend Server
📍 Server: http://localhost:8001
🗄️  Database: PostgreSQL with persistent storage
✅ Default users initialized
```

### 4. Test the Application

Visit: http://localhost:8001/health

You should see:
```json
{
  "status": "healthy",
  "database": "PostgreSQL",
  "users": 3,
  "documents": 0
}
```

## 📊 Database Schema

The application automatically creates these tables:

### users
- id (UUID, Primary Key)
- email (Unique)
- password_hash
- full_name
- role (user/admin/superadmin)
- is_active
- created_at
- updated_at

### documents
- id (UUID, Primary Key)
- user_id (Foreign Key)
- filename
- original_filename
- file_path
- file_size
- content_type
- category
- privacy_score
- is_shared
- is_verified
- blockchain_hash
- created_at
- updated_at

### shares
- id (UUID, Primary Key)
- document_id (Foreign Key)
- user_id (Foreign Key)
- share_token (Unique)
- document_name
- created_at
- expires_at
- access_count
- max_access
- status

### access_logs
- id (UUID, Primary Key)
- user_id (Foreign Key)
- action
- timestamp
- ip_address
- device
- location
- status

## 🔐 Default Users

The application creates these users automatically on first startup:

```
Super Admin:
  Email: superadmin@datavault.com
  Password: SuperAdmin2024!

Admin:
  Email: admin@datavault.com
  Password: Admin2024!

Test User:
  Email: user@example.com
  Password: password
```

These users are created ONCE and persist forever!

## 🐛 Troubleshooting

### "Could not connect to server"

**Problem:** PostgreSQL is not running

**Solution:**
- Windows: Start PostgreSQL service from Services
- Mac: `brew services start postgresql`
- Linux: `sudo systemctl start postgresql`

### "password authentication failed"

**Problem:** Wrong credentials in DATABASE_URL

**Solution:**
1. Check your PostgreSQL password
2. Update `backend/.env` with correct credentials
3. Restart the backend

### "database does not exist"

**Problem:** Database not created

**Solution:**
```bash
cd backend
python setup_postgres.py
```

### "relation does not exist"

**Problem:** Tables not created

**Solution:**
- Stop the backend (Ctrl+C)
- Start it again: `python app.py`
- Tables are created automatically on startup

### Fallback to SQLite

If PostgreSQL is not available, the application automatically falls back to SQLite:
- Database file: `backend/datavault.db`
- Still persistent, but not as robust as PostgreSQL
- Good for development, not recommended for production

## 🎯 Testing Upload Functionality

### 1. Login
```bash
curl -X POST http://localhost:8001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password"}'
```

Save the `access_token` from the response.

### 2. Upload Document
```bash
curl -X POST http://localhost:8001/api/documents/upload \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -F "file=@/path/to/your/document.pdf"
```

### 3. Get Documents
```bash
curl -X GET http://localhost:8001/api/documents/ \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

### 4. Verify in Database

```bash
psql -U postgres -d datavault
SELECT * FROM users;
SELECT * FROM documents;
\q
```

## 📁 File Storage

- Uploaded files are stored in: `backend/uploads/`
- File metadata is stored in PostgreSQL
- Both must exist for documents to work properly

## 🔄 Backup and Restore

### Backup Database
```bash
pg_dump -U postgres datavault > datavault_backup.sql
```

### Restore Database
```bash
psql -U postgres datavault < datavault_backup.sql
```

## 🚀 Production Deployment

For production, use a managed PostgreSQL service:
- AWS RDS
- Google Cloud SQL
- Azure Database for PostgreSQL
- Heroku Postgres
- DigitalOcean Managed Databases

Update `DATABASE_URL` in `.env` with your production database URL.

## 📞 Support

If you encounter issues:
1. Check PostgreSQL is running
2. Verify credentials in `.env`
3. Run `python setup_postgres.py`
4. Check backend logs for errors
5. Test with `curl` commands above

---

**Status**: ✅ Ready for Production
**Database**: PostgreSQL with full persistence
**Last Updated**: March 18, 2026
