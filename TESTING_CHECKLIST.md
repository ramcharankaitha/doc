# DataVault Secure - Testing Checklist

## 🧪 Complete Testing Guide

This checklist ensures all features of DataVault Secure are working correctly.

## ✅ Pre-Testing Setup

- [ ] Backend running on `http://localhost:8000`
- [ ] Frontend running on `http://localhost:3000`
- [ ] Supabase database configured and schema loaded
- [ ] Environment variables set correctly
- [ ] Browser console open (F12) for debugging

## 🔐 Authentication Flow

### User Registration
- [ ] Navigate to landing page
- [ ] Click "Get Started" or "Sign in"
- [ ] Fill registration form with valid data
- [ ] Submit registration
- [ ] Verify OTP is sent (check console/email)
- [ ] Enter OTP and verify account
- [ ] Check user is created in Supabase database
- [ ] Verify JWT token is stored in localStorage

**Expected Result:** User successfully registered and logged in

### User Login
- [ ] Navigate to login page
- [ ] Enter registered email and password
- [ ] Submit login form
- [ ] Verify OTP is sent
- [ ] Enter OTP
- [ ] Check redirect to dashboard
- [ ] Verify token in localStorage
- [ ] Check user session is active

**Expected Result:** User successfully logged in and redirected to dashboard

### Logout
- [ ] Click logout button
- [ ] Verify token is removed from localStorage
- [ ] Check redirect to landing page
- [ ] Try accessing dashboard (should redirect to login)

**Expected Result:** User successfully logged out

## 📤 Document Management

### Document Upload
- [ ] Navigate to user dashboard
- [ ] Click "Upload Document" button
- [ ] Select a document file (PDF, JPG, PNG)
- [ ] Choose document category (Aadhaar, PAN, etc.)
- [ ] Submit upload
- [ ] Verify OCR processing starts
- [ ] Check document appears in document list
- [ ] Verify document metadata is correct
- [ ] Check file is stored in Supabase Storage
- [ ] Verify blockchain hash is generated

**Expected Result:** Document uploaded, processed, and displayed

### Document List
- [ ] View all uploaded documents
- [ ] Check document cards show correct info
- [ ] Verify document icons match categories
- [ ] Check upload dates are correct
- [ ] Verify status badges (Verified, Blockchain, etc.)

**Expected Result:** All documents displayed correctly

### Document View
- [ ] Click "View" on a document
- [ ] Verify document preview loads
- [ ] Check document details are correct
- [ ] Verify OCR extracted data is shown
- [ ] Check blockchain verification status

**Expected Result:** Document details displayed correctly

### Document Delete
- [ ] Click delete on a document
- [ ] Confirm deletion
- [ ] Verify document is removed from list
- [ ] Check document is deleted from database
- [ ] Verify file is removed from storage

**Expected Result:** Document successfully deleted

## 🔗 Secure Sharing

### Create Share Link
- [ ] Click "Share" on a document
- [ ] Set access limit (e.g., 1 view)
- [ ] Set expiry duration (e.g., 1 hour)
- [ ] Enable OTP verification
- [ ] Enable/disable download
- [ ] Enable auto-masking
- [ ] Enable self-destruct
- [ ] Generate secure link
- [ ] Verify link is created
- [ ] Copy link to clipboard

**Expected Result:** Secure share link generated with all controls

### Access Share Link
- [ ] Open share link in incognito/private window
- [ ] Verify OTP is required
- [ ] Enter OTP
- [ ] View document
- [ ] Check sensitive data is masked
- [ ] Verify download button state (enabled/disabled)
- [ ] Check view count increments
- [ ] Try accessing again (should fail if view limit reached)

**Expected Result:** Share link works with all configured controls

### Revoke Share Link
- [ ] Go to "Shared Links" section
- [ ] Click "Revoke" on an active link
- [ ] Confirm revocation
- [ ] Try accessing revoked link
- [ ] Verify access is denied

**Expected Result:** Share link successfully revoked

### Self-Destructing Link
- [ ] Create share link with self-destruct enabled
- [ ] Access link once
- [ ] Try accessing again
- [ ] Verify link is destroyed

**Expected Result:** Link self-destructs after first view

## 🛡️ Privacy & Security

### Privacy Score
- [ ] View privacy score on dashboard
- [ ] Check score calculation is correct
- [ ] View recommendations
- [ ] Follow a recommendation (e.g., enable 2FA)
- [ ] Verify score updates

**Expected Result:** Privacy score displayed and updates correctly

### Access History
- [ ] View access history table
- [ ] Check all document accesses are logged
- [ ] Verify timestamps are correct
- [ ] Check device and location info
- [ ] Verify risk levels are assigned

**Expected Result:** Complete access history displayed

### Security Alerts
- [ ] Trigger suspicious activity (multiple failed logins)
- [ ] Check alert appears in dashboard
- [ ] Verify alert details are correct
- [ ] Dismiss or resolve alert
- [ ] Check alert status updates

**Expected Result:** Security alerts generated and displayed

## 👮 Admin Dashboard

### Access Admin Dashboard
- [ ] Navigate to `/admin.html`
- [ ] Login with admin credentials
- [ ] Verify admin dashboard loads
- [ ] Check all metrics are displayed

**Expected Result:** Admin dashboard accessible and functional

### Security Monitoring
- [ ] View real-time security alerts
- [ ] Check high-risk users list
- [ ] View access logs
- [ ] Filter logs by risk level
- [ ] Export logs to CSV

**Expected Result:** Security monitoring tools working

### User Management
- [ ] View user list
- [ ] Search for specific user
- [ ] View user risk score
- [ ] Lock a user account
- [ ] Unlock user account
- [ ] Force identity verification

**Expected Result:** User management controls working

### Voice Bot Calls
- [ ] Select high-risk user
- [ ] Trigger voice bot call
- [ ] Verify call is initiated (check console/logs)
- [ ] Check call status updates

**Expected Result:** Voice bot call triggered successfully

### IP Blocking
- [ ] Identify suspicious IP
- [ ] Block IP address
- [ ] Verify IP is added to blocklist
- [ ] Try accessing from blocked IP
- [ ] Verify access is denied

**Expected Result:** IP blocking working correctly

## 👑 Super Admin Dashboard

### Access Super Admin Dashboard
- [ ] Navigate to `/superadmin.html`
- [ ] Login with super admin credentials
- [ ] Verify super admin dashboard loads
- [ ] Check platform overview metrics

**Expected Result:** Super admin dashboard accessible

### Admin Management
- [ ] View admin list
- [ ] Add new admin
- [ ] Assign admin role
- [ ] Edit admin permissions
- [ ] Remove admin
- [ ] Verify changes in database

**Expected Result:** Admin management working

### AI Configuration
- [ ] Adjust anomaly sensitivity slider
- [ ] Change risk score threshold
- [ ] Modify max share duration
- [ ] Set auto-lock trigger score
- [ ] Save configuration
- [ ] Verify settings are applied

**Expected Result:** AI configuration updates successfully

### Platform Analytics
- [ ] View total users count
- [ ] Check documents stored
- [ ] View security alerts count
- [ ] Check blockchain verifications
- [ ] View system health status

**Expected Result:** Analytics displayed correctly

### Document Categories
- [ ] View document category breakdown
- [ ] Check counts for each category
- [ ] Verify percentages are correct

**Expected Result:** Category statistics accurate

### System Status
- [ ] Check blockchain status
- [ ] Verify AI Guardian status
- [ ] Check OCR service status
- [ ] View voice bot API status
- [ ] Check database connection
- [ ] Verify storage status

**Expected Result:** All system components showing correct status

## 🤖 AI/ML Features

### OCR Document Scanning
- [ ] Upload document with text
- [ ] Verify OCR extracts text correctly
- [ ] Check extracted data accuracy
- [ ] Verify document type detection
- [ ] Check confidence scores

**Expected Result:** OCR accurately extracts document data

### Anomaly Detection
- [ ] Perform normal activity
- [ ] Perform suspicious activity (multiple logins, bulk downloads)
- [ ] Check anomaly is detected
- [ ] Verify risk score increases
- [ ] Check alert is generated

**Expected Result:** Anomaly detection working correctly

### Risk Scoring
- [ ] View user risk score
- [ ] Perform various activities
- [ ] Check risk score updates
- [ ] Verify score calculation logic
- [ ] Check risk level thresholds

**Expected Result:** Risk scoring accurate and responsive

### Smart Data Masking
- [ ] Share document with masking enabled
- [ ] View shared document
- [ ] Verify sensitive data is masked (e.g., XXXX XXXX 1234)
- [ ] Check masking patterns are correct

**Expected Result:** Data masking working correctly

## ⛓️ Blockchain Features

### Document Hash Generation
- [ ] Upload document
- [ ] Verify blockchain hash is generated
- [ ] Check hash is stored in database
- [ ] Verify hash format is correct

**Expected Result:** Blockchain hash generated for documents

### Document Verification
- [ ] View document details
- [ ] Check blockchain verification status
- [ ] Verify document hasn't been tampered
- [ ] Try modifying document
- [ ] Check verification fails for modified document

**Expected Result:** Blockchain verification working

## 🔔 Notifications

### Success Notifications
- [ ] Perform successful action (upload, share, etc.)
- [ ] Verify success notification appears
- [ ] Check notification message is correct
- [ ] Verify notification auto-dismisses

**Expected Result:** Success notifications displayed

### Error Notifications
- [ ] Trigger error (invalid input, failed request)
- [ ] Verify error notification appears
- [ ] Check error message is helpful
- [ ] Dismiss notification manually

**Expected Result:** Error notifications displayed

### Warning Notifications
- [ ] Trigger warning condition
- [ ] Verify warning notification appears
- [ ] Check warning message is clear

**Expected Result:** Warning notifications displayed

## 📱 Responsive Design

### Desktop View
- [ ] Test on desktop browser (1920x1080)
- [ ] Verify all elements are visible
- [ ] Check layout is correct
- [ ] Test all interactions

**Expected Result:** Perfect desktop experience

### Tablet View
- [ ] Test on tablet size (768x1024)
- [ ] Verify responsive layout
- [ ] Check navigation works
- [ ] Test all features

**Expected Result:** Good tablet experience

### Mobile View
- [ ] Test on mobile size (375x667)
- [ ] Verify mobile-friendly layout
- [ ] Check touch interactions
- [ ] Test navigation menu

**Expected Result:** Mobile-optimized experience

## 🌐 Browser Compatibility

- [ ] Test on Chrome
- [ ] Test on Firefox
- [ ] Test on Safari
- [ ] Test on Edge
- [ ] Verify consistent behavior across browsers

**Expected Result:** Works on all major browsers

## ⚡ Performance

### Load Times
- [ ] Measure page load time (< 3 seconds)
- [ ] Check API response times (< 500ms)
- [ ] Verify image loading is optimized
- [ ] Check no memory leaks

**Expected Result:** Fast and responsive

### Large File Upload
- [ ] Upload large document (10MB+)
- [ ] Verify upload progress indicator
- [ ] Check upload completes successfully
- [ ] Verify no timeout errors

**Expected Result:** Large files upload successfully

## 🔒 Security Testing

### Authentication Security
- [ ] Try accessing protected routes without token
- [ ] Verify redirect to login
- [ ] Try using expired token
- [ ] Check token refresh works

**Expected Result:** Authentication properly secured

### Input Validation
- [ ] Try SQL injection in forms
- [ ] Try XSS attacks
- [ ] Submit invalid data
- [ ] Verify proper error handling

**Expected Result:** All inputs properly validated

### CORS
- [ ] Check CORS headers are correct
- [ ] Verify cross-origin requests work
- [ ] Test from different origins

**Expected Result:** CORS configured correctly

## 📊 Database

### Data Persistence
- [ ] Create data (user, document, share)
- [ ] Refresh page
- [ ] Verify data persists
- [ ] Check database records

**Expected Result:** Data persists correctly

### Data Integrity
- [ ] Check foreign key constraints
- [ ] Verify cascading deletes work
- [ ] Check unique constraints
- [ ] Verify data types are correct

**Expected Result:** Database integrity maintained

## 🐛 Error Handling

### Network Errors
- [ ] Disconnect internet
- [ ] Try performing actions
- [ ] Verify error messages appear
- [ ] Reconnect and retry

**Expected Result:** Graceful error handling

### Server Errors
- [ ] Stop backend server
- [ ] Try API calls
- [ ] Verify error messages
- [ ] Restart server and retry

**Expected Result:** Clear error messages displayed

## 📝 Final Checks

- [ ] All features working as expected
- [ ] No console errors
- [ ] No broken links
- [ ] All images loading
- [ ] All scripts loading
- [ ] Proper error handling everywhere
- [ ] Good user experience
- [ ] Fast performance
- [ ] Secure implementation
- [ ] Clean code
- [ ] Documentation complete

## 🎉 Testing Complete!

If all items are checked, your DataVault Secure application is fully functional and ready for deployment!

---

**Testing Date:** _____________

**Tested By:** _____________

**Status:** ⬜ Pass | ⬜ Fail | ⬜ Needs Review

**Notes:**
_____________________________________________
_____________________________________________
_____________________________________________
