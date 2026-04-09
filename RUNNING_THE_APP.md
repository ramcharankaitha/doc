# Running DataVault Secure - Quick Guide

## 🚀 Quick Start (Local Development)

### Prerequisites
- Python 3.9+
- Node.js (for local server)
- Supabase account (free)

### Step 1: Set Up Supabase

1. Go to [supabase.com](https://supabase.com) and create a free account
2. Create a new project
3. Go to Project Settings → API
4. Copy your:
   - Project URL
   - Anon/Public Key
   - Service Role Key (for backend)

5. Go to SQL Editor and run the schema from `backend/database/init.sql`

### Step 2: Configure Backend

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file from template:
```bash
cp .env.example .env
```

5. Edit `.env` with your Supabase credentials:
```env
DATABASE_URL=postgresql://postgres:[YOUR-PASSWORD]@[YOUR-PROJECT-REF].supabase.co:5432/postgres
SUPABASE_URL=https://[YOUR-PROJECT-REF].supabase.co
SUPABASE_KEY=[YOUR-ANON-KEY]
SECRET_KEY=[GENERATE-RANDOM-STRING]
```

6. Run the backend:
```bash
uvicorn app.main:app --reload
```

Backend will be available at: `http://localhost:8000`

### Step 3: Configure Frontend

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Edit `config.js`:
```javascript
const CONFIG = {
  API_BASE_URL: 'http://localhost:8000',
  SUPABASE_URL: 'https://[YOUR-PROJECT-REF].supabase.co',
  SUPABASE_ANON_KEY: '[YOUR-ANON-KEY]'
};
```

3. Serve frontend (choose one):

**Option A: Python HTTP Server**
```bash
python -m http.server 3000
```

**Option B: Node.js HTTP Server**
```bash
npx http-server -p 3000
```

**Option C: VS Code Live Server**
- Install "Live Server" extension
- Right-click `index.html` → "Open with Live Server"

Frontend will be available at: `http://localhost:3000`

## 🌐 Testing the Application

### 1. Landing Page
- Open `http://localhost:3000/index.html`
- Explore features, pricing, and information

### 2. User Registration
- Click "Get Started" or "Sign in"
- Register a new account
- Verify OTP (check console for OTP in development)

### 3. User Dashboard
- Upload a document
- View privacy score
- Create a secure share link
- Check access history

### 4. Admin Dashboard
- Navigate to `http://localhost:3000/admin.html`
- View security alerts
- Monitor user activity
- Test voice bot calls

### 5. Super Admin Dashboard
- Navigate to `http://localhost:3000/superadmin.html`
- Manage admins
- Configure AI settings
- View platform analytics

## 🔧 API Testing

### Using cURL

**Register User:**
```bash
curl -X POST http://localhost:8000/api/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePass123!",
    "full_name": "Test User"
  }'
```

**Login:**
```bash
curl -X POST http://localhost:8000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "SecurePass123!"
  }'
```

**Upload Document:**
```bash
curl -X POST http://localhost:8000/api/documents/upload \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -F "file=@/path/to/document.pdf" \
  -F "category=aadhaar"
```

### Using Postman

1. Import the API collection (create from endpoints in `PROJECT_DOCUMENTATION.md`)
2. Set environment variable `BASE_URL` to `http://localhost:8000`
3. Test all endpoints

## 📱 Browser Console Testing

Open browser console (F12) and test API directly:

```javascript
// Test API connection
fetch('http://localhost:8000/health')
  .then(r => r.json())
  .then(console.log);

// Register user
fetch('http://localhost:8000/api/auth/register', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'test@example.com',
    password: 'SecurePass123!',
    full_name: 'Test User'
  })
})
.then(r => r.json())
.then(console.log);
```

## 🐛 Troubleshooting

### Backend Issues

**Port already in use:**
```bash
# Use different port
uvicorn app.main:app --reload --port 8001
```

**Database connection error:**
- Check Supabase credentials in `.env`
- Verify database schema is created
- Check Supabase project is active

**Import errors:**
```bash
# Reinstall dependencies
pip install -r requirements.txt --force-reinstall
```

### Frontend Issues

**CORS errors:**
- Ensure backend CORS is configured correctly
- Check `API_BASE_URL` in `config.js`
- Use same protocol (http/https)

**API not connecting:**
- Verify backend is running
- Check browser console for errors
- Verify API URL in `config.js`

**Scripts not loading:**
- Check file paths are correct
- Ensure all JS files exist in `assets/js/`
- Check browser console for 404 errors

## 🔍 Checking Logs

### Backend Logs
Backend logs appear in terminal where you ran `uvicorn`:
```
INFO:     127.0.0.1:52000 - "POST /api/auth/login HTTP/1.1" 200 OK
```

### Frontend Logs
Open browser console (F12) to see:
- API requests
- Errors
- Debug messages

### Database Logs
Check Supabase dashboard:
- Database → Logs
- API → Logs

## 📊 Monitoring

### Backend Health Check
```bash
curl http://localhost:8000/health
```

Expected response:
```json
{
  "status": "healthy",
  "timestamp": "2025-03-14T10:30:00Z"
}
```

### API Documentation
Visit: `http://localhost:8000/docs`
- Interactive API documentation
- Test endpoints directly
- View request/response schemas

## 🚀 Production Deployment

See `DEPLOYMENT_GUIDE.md` for detailed production deployment instructions.

### Quick Deploy

**Backend (Render):**
1. Push code to GitHub
2. Connect Render to repository
3. Add environment variables
4. Deploy

**Frontend (Vercel):**
1. Push code to GitHub
2. Import project in Vercel
3. Update `config.js` with production API URL
4. Deploy

## 💡 Tips

1. **Use API Documentation:** Visit `/docs` for interactive API testing
2. **Check Console:** Always check browser console for errors
3. **Test Incrementally:** Test each feature separately
4. **Use Postman:** Great for testing API endpoints
5. **Monitor Logs:** Keep terminal and console open while testing

## 📞 Support

If you encounter issues:
1. Check this guide
2. Review `PROJECT_DOCUMENTATION.md`
3. Check `QUICKSTART.md`
4. Review error messages carefully
5. Check Supabase dashboard for database issues

---

**Happy Coding! 🚀**
