# Document Upload Guide

## ✅ Upload Feature Status: FULLY FUNCTIONAL

The document upload functionality has been tested and verified to be working perfectly.

## 🚀 How to Use

### 1. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8001
- **API Docs**: http://localhost:8001/api/docs

### 2. Login Credentials
```
Regular User:
  Email: user@example.com
  Password: password

Admin:
  Email: admin@datavault.com
  Password: Admin2024!

Super Admin:
  Email: superadmin@datavault.com
  Password: SuperAdmin2024!
```

### 3. Upload Documents

#### Via Dashboard (http://localhost:3000/dashboard.html)
1. Login with your credentials
2. Click the "+ Upload Document" button or the upload zone
3. Select a file (images: JPG, PNG or PDF files)
4. File will be uploaded automatically
5. Document will appear in your documents grid

#### Via API
```bash
# 1. Login to get token
curl -X POST http://localhost:8001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password"}'

# 2. Upload document
curl -X POST http://localhost:8001/api/documents/upload \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  -F "file=@/path/to/your/document.pdf"
```

## 📋 Supported File Types
- **Images**: JPG, JPEG, PNG
- **Documents**: PDF
- **Max Size**: 10 MB per file

## ✨ Features Working

### Backend (Port 8001)
- ✅ User authentication (JWT tokens)
- ✅ File upload with validation
- ✅ File type checking
- ✅ File size validation (10MB limit)
- ✅ Unique filename generation
- ✅ File storage in uploads directory
- ✅ Document metadata tracking
- ✅ Get documents list
- ✅ Risk score calculation
- ✅ Access logs tracking
- ✅ CORS properly configured

### Frontend (Port 3000)
- ✅ Login page
- ✅ Dashboard with document grid
- ✅ Upload button and zone
- ✅ File selection dialog
- ✅ Upload progress notifications
- ✅ Document display with icons
- ✅ Privacy score display
- ✅ Access history
- ✅ Share functionality

## 🔧 Technical Details

### Upload Endpoint
```
POST /api/documents/upload
Authorization: Bearer <token>
Content-Type: multipart/form-data

Body: file (binary)
```

### Response Format
```json
{
  "message": "Document uploaded successfully",
  "id": "uuid",
  "filename": "original_name.pdf",
  "category": "document",
  "size": "1.5 KB",
  "uploaded_at": "2024-03-18T12:00:00Z",
  "privacy_score": 90,
  "is_shared": false,
  "icon": "📄",
  "file_path": "uploads/unique_id.pdf",
  "file_size": 1536,
  "content_type": "application/pdf"
}
```

## 🐛 Troubleshooting

### Upload Not Working?
1. **Check servers are running**:
   - Backend: http://localhost:8001/health
   - Frontend: http://localhost:3000

2. **Check you're logged in**:
   - Token should be stored in localStorage
   - Check browser console for auth errors

3. **Check file type**:
   - Only JPG, PNG, and PDF files are allowed
   - Max size is 10MB

4. **Check browser console**:
   - Open DevTools (F12)
   - Look for error messages in Console tab
   - Check Network tab for failed requests

### Common Issues

**"File type not allowed"**
- Solution: Use JPG, PNG, or PDF files only

**"File too large"**
- Solution: Compress file to under 10MB

**"Invalid token" or "Unauthorized"**
- Solution: Log out and log in again

**Upload button disabled**
- Solution: Make sure you're logged in first

## 📁 File Storage

Uploaded files are stored in:
```
backend/uploads/
```

Each file gets a unique UUID-based filename to prevent conflicts.

## 🎯 Test Results

All tests passing:
- ✅ Health Check
- ✅ Login
- ✅ Document Upload
- ✅ Get Documents
- ✅ Risk Score
- ✅ Access Logs

## 🔐 Security Features

- JWT token authentication
- File type validation
- File size limits
- Unique filename generation
- Secure file storage
- Access logging
- CORS protection

## 📞 Support

If you encounter any issues:
1. Check this guide first
2. Verify servers are running
3. Check browser console for errors
4. Review backend logs in terminal
5. Ensure you're using supported file types

---

**Last Updated**: March 18, 2026
**Status**: ✅ Fully Operational
