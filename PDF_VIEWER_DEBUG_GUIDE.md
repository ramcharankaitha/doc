# PDF Viewer Debugging Guide

## Current Issue
PDF viewer shows "Failed to fetch" error when trying to view documents.

## Debugging Steps

### 1. Use the Debug Tool
Open `test_pdf_viewer.html` in your browser and follow these steps:

1. **Step 1: Login**
   - Click "Login as user@example.com"
   - Should show: ✅ Login successful with token

2. **Step 2: Get Documents**
   - Click "Load Documents"
   - Should show: List of documents with IDs
   - First document ID will be auto-filled

3. **Step 3: Get Document Details**
   - Click "Get Document Info"
   - Should show: Document metadata including file path

4. **Step 4: Fetch PDF File**
   - Click "Fetch PDF File"
   - Should show: Blob created with size and type
   - **This is where the error likely occurs**

5. **Step 5: Display PDF**
   - Click "Display PDF in Viewer"
   - Should show: PDF in iframe below

### 2. Check Browser Console
Open Developer Tools (F12) and check:
- Network tab: Look for failed requests
- Console tab: Look for error messages
- Check the exact error message and status code

### 3. Common Issues and Solutions

#### Issue: "Failed to fetch" or CORS Error
**Cause**: Backend not allowing cross-origin requests
**Solution**: Check backend CORS configuration

```python
# In backend/app_postgres.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Should allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

#### Issue: "Not authenticated" or 401 Error
**Cause**: Token not being sent or invalid
**Solution**: 
1. Check if token exists in localStorage
2. Verify token format in Authorization header
3. Check token expiration

#### Issue: "Document not found" or 404 Error
**Cause**: File doesn't exist on disk or wrong document ID
**Solution**:
1. Check if file exists in `backend/uploads/` folder
2. Verify document ID is correct
3. Check database record has correct file_path

#### Issue: "File not found on disk"
**Cause**: File was deleted or moved
**Solution**:
1. Check `backend/uploads/` folder
2. Re-upload the document
3. Verify file permissions

### 4. Manual API Testing

#### Test Login
```bash
curl -X POST http://localhost:8001/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"user@example.com","password":"password"}'
```

#### Test Get Documents
```bash
curl -X GET http://localhost:8001/api/documents \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

#### Test Get File
```bash
curl -X GET http://localhost:8001/api/documents/DOCUMENT_ID/file \
  -H "Authorization: Bearer YOUR_TOKEN_HERE" \
  --output test.pdf
```

### 5. Check Backend Logs
Look at the backend console output for:
- Incoming requests
- Authentication errors
- File access errors
- Database errors

### 6. Verify File Exists
Check if the uploaded files exist:
```bash
# Windows
dir backend\uploads

# Linux/Mac
ls -la backend/uploads/
```

### 7. Check Database
Verify document records in PostgreSQL:
```sql
SELECT id, original_filename, file_path, content_type, user_id 
FROM documents 
ORDER BY created_at DESC 
LIMIT 10;
```

## Quick Fixes

### Fix 1: Clear Browser Cache
1. Press `Ctrl + Shift + Delete`
2. Clear cached images and files
3. Reload page with `Ctrl + F5`

### Fix 2: Restart Backend
1. Stop backend server (Ctrl+C)
2. Restart: `python backend/app_postgres.py`
3. Wait for "Application startup complete"

### Fix 3: Check Token
```javascript
// In browser console
console.log(localStorage.getItem('access_token'));
```

### Fix 4: Test Direct File Access
Try accessing file directly in browser:
```
http://localhost:8001/api/documents/DOCUMENT_ID/file
```
(Will fail due to auth, but check the error message)

## Expected Behavior

### Successful Flow:
1. User clicks "View" button
2. Frontend fetches document metadata
3. Frontend fetches file with Bearer token
4. Backend validates token
5. Backend checks file exists
6. Backend returns file as FileResponse
7. Frontend creates Blob from response
8. Frontend creates Blob URL
9. Frontend displays in iframe
10. PDF renders in viewer

### Error Points:
- ❌ Token invalid/expired → 401 error
- ❌ Document not found → 404 error
- ❌ File not on disk → 404 error
- ❌ CORS issue → Network error
- ❌ Backend not running → Connection refused

## Debug Checklist

- [ ] Backend server is running on port 8001
- [ ] User is logged in (token in localStorage)
- [ ] Documents exist in database
- [ ] Files exist in backend/uploads/ folder
- [ ] CORS is properly configured
- [ ] Browser cache is cleared
- [ ] No console errors
- [ ] Network tab shows successful requests
- [ ] Token is valid and not expired

## Still Not Working?

If PDF viewer still doesn't work after all checks:

1. **Check the exact error message** in browser console
2. **Check backend logs** for the actual error
3. **Use the debug tool** (`test_pdf_viewer.html`) to isolate the issue
4. **Test with curl** to verify backend is working
5. **Check file permissions** on uploads folder
6. **Verify PostgreSQL** connection and data

## Contact Information

If you need help:
1. Provide the exact error message from console
2. Provide backend log output
3. Provide network tab screenshot
4. Specify which step in debug tool fails

---

**Last Updated**: March 18, 2026  
**Status**: Debugging in progress