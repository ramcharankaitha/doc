# Admin & Super Admin Panel Testing Guide

## Overview
This guide provides step-by-step instructions for testing all functionalities in the Admin and Super Admin panels.

## Prerequisites
1. Backend server running on `http://localhost:8001`
2. Frontend accessible (open `frontend/admin.html` or `frontend/superadmin.html`)
3. PostgreSQL database set up with default users

## Default Credentials

### Super Admin
- Email: `superadmin@datavault.com`
- Password: `SuperAdmin2024!`

### Admin
- Email: `admin@datavault.com`
- Password: `Admin2024!`

### Regular User
- Email: `user@example.com`
- Password: `password`

---

## Admin Panel Testing (`frontend/admin.html`)

### 1. Login as Admin
1. Navigate to `frontend/login.html`
2. Enter admin credentials
3. Should redirect to admin dashboard

### 2. Security Metrics Dashboard
**Expected Behavior:**
- 4 metric cards display:
  - High Risk Users (count)
  - Active Alerts (count)
  - Active Users (count)
  - AI Detections (count)
- Metrics auto-refresh every 30 seconds

**Test:**
- Verify numbers are displayed
- Check that metrics update when data changes

### 3. Security Alerts Feed
**Features:**
- Real-time alert display
- Risk level indicators (HIGH/MEDIUM/LOW)
- Alert details (user, event, location, device, IP)
- Action buttons for each alert

**Test Actions:**
- **Lock Account Button**: Click to lock a user account
  - Should show confirmation dialog
  - Should display success notification
  - Should reload alerts
  
- **Voice Call Button**: Click to trigger security call
  - Should show "Initiating voice call..." notification
  - Should display success message
  
- **Dismiss Button**: Click to dismiss an alert
  - Should remove alert from feed
  - Should show success notification

### 4. Access Logs Table
**Features:**
- Real-time access log display
- Columns: User & Document, Device, Location, Time, Risk
- Risk level color coding

**Test:**
- Verify logs are displayed
- Check risk level badges (HIGH/MEDIUM/LOW)
- Verify time formatting

### 5. High Risk Users Panel
**Features:**
- Displays users with risk score > 60
- Shows risk score with progress bar
- Click to view user details

**Test:**
- Click on a risk user card
- Should show notification with user details

### 6. Voice Bot Security Call
**Features:**
- Select target user from dropdown
- Trigger security call with pre-defined script

**Test:**
- Select a user from dropdown
- Click "Trigger Security Call Now"
- Should show success notification

### 7. Quick Security Actions
**Test Each Button:**
- **Lock User Account**: Should show confirmation and lock user
- **Revoke All Share Links**: Should show success notification
- **Force Identity Verify**: Should show SMS sent notification
- **Block Suspicious IP**: Should show IP blocked notification
- **Suspend Account**: Should show confirmation dialog

---

## Super Admin Panel Testing (`frontend/superadmin.html`)

### 1. Login as Super Admin
1. Navigate to `frontend/login.html`
2. Enter superadmin credentials
3. Should redirect to superadmin dashboard

### 2. Platform Overview Bar
**Expected Display:**
- Total Users count
- Total Documents count
- Today's Shares count
- Flagged Users count
- System Health percentage with circular progress

**Test:**
- Verify all statistics are displayed
- Check system health circle animation

### 3. Metric Tiles
**4 Tiles Display:**
- Active Users (Now)
- Security Alerts Today
- Docs Uploaded Today
- Blockchain Verifications

**Test:**
- Verify all metrics show numbers
- Check trend indicators (↑/↓)

### 4. Admin Management
**Features:**
- List all admins with roles
- Add new admin
- Edit admin (placeholder)
- Remove admin

**Test Add Admin:**
1. Click "+ Add Admin" button
2. Enter email (e.g., `newadmin@test.com`)
3. Enter password (e.g., `Admin123!`)
4. Enter full name (e.g., `New Admin`)
5. Enter phone (optional)
6. Should show success notification
7. New admin should appear in list

**Test Remove Admin:**
1. Click "Remove" button on an admin (not superadmin)
2. Confirm removal
3. Should show success notification
4. Admin should be removed from list

### 5. AI Privacy Guardian Config
**Features:**
- 4 slider controls:
  - Anomaly Sensitivity (0-100%)
  - Risk Score Alert Threshold (0-100)
  - Max Share Duration (1-72 hours)
  - Auto-Lock Trigger Score (50-100)
- 3 toggle switches:
  - Auto-lock high risk accounts
  - Auto voice-call on HIGH risk
  - Download restrictions enabled

**Test:**
1. Adjust each slider
2. Verify value updates in real-time
3. Toggle switches on/off
4. Click "Save Changes"
5. Should show success notification

### 6. Document Categories
**Features:**
- Lists 5 document categories:
  - Aadhaar Cards
  - PAN Cards
  - Passports
  - Certificates
  - Medical Records
- Shows count and progress bar for each

**Test:**
- Verify all categories are displayed
- Check counts and progress bars

### 7. System Analytics
**Features:**
- 6 progress bars showing:
  - Documents stored
  - Document shares
  - Security alerts
  - Voice calls sent
  - OCR scans done
  - Blockchain verifications

**Test:**
- Verify all bars are displayed
- Check values and percentages

### 8. Blockchain & System Status
**Features:**
- 4 status cards:
  - Blockchain Active
  - AI Guardian Module
  - OCR Service
  - Voice Bot API
- 3 system alerts:
  - Supabase PostgreSQL status
  - Supabase Storage status
  - Render Backend status

**Test:**
- Verify all status badges show correct state
- Check system alerts display

### 9. Global Security Policy Engine
**Features:**
- 3 dropdown selectors:
  - Max Share Link Duration
  - Default Max View Limit
  - Global Download Policy

**Test:**
1. Change each dropdown value
2. Click "Deploy Policy Update"
3. Should show success notification

---

## Auto-Refresh Testing

### Admin Panel
- Metrics refresh every 30 seconds
- Alerts refresh every 30 seconds
- Access logs refresh every 30 seconds

### Super Admin Panel
- Platform stats refresh every 60 seconds
- System status refresh every 60 seconds

**Test:**
1. Open browser console
2. Wait for auto-refresh interval
3. Check console logs for refresh activity

---

## Error Handling Testing

### Test Network Errors
1. Stop the backend server
2. Try to perform any action
3. Should show error notification

### Test Authentication Errors
1. Clear localStorage
2. Refresh page
3. Should redirect to login page

### Test Permission Errors
1. Login as regular user
2. Try to access admin panel directly
3. Should show "Access denied" and redirect

---

## Browser Compatibility Testing

Test in:
- Chrome/Edge (Chromium)
- Firefox
- Safari

Verify:
- All UI elements render correctly
- All buttons work
- Notifications appear
- Auto-refresh works

---

## Performance Testing

### Load Testing
1. Open browser DevTools (Network tab)
2. Load admin/superadmin panel
3. Check:
   - Initial load time < 2 seconds
   - API calls complete < 500ms
   - No failed requests

### Memory Testing
1. Open browser DevTools (Performance tab)
2. Let panel run for 5 minutes with auto-refresh
3. Check:
   - No memory leaks
   - Smooth animations
   - No console errors

---

## Common Issues & Solutions

### Issue: "Failed to fetch" error
**Solution:** Ensure backend is running on port 8001

### Issue: "Access denied" message
**Solution:** Login with correct admin/superadmin credentials

### Issue: Metrics not updating
**Solution:** Check browser console for errors, verify API endpoints

### Issue: Buttons not working
**Solution:** Clear browser cache, hard refresh (Ctrl+Shift+R)

### Issue: Notifications not appearing
**Solution:** Check if notifications are blocked in browser settings

---

## Success Criteria

✅ All metrics display correctly
✅ All buttons trigger expected actions
✅ All API calls succeed
✅ Notifications appear for all actions
✅ Auto-refresh works without errors
✅ No console errors
✅ Smooth UI performance
✅ Proper error handling
✅ Authentication works correctly
✅ Role-based access control works

---

## Next Steps After Testing

1. Document any bugs found
2. Test with real user data
3. Perform security audit
4. Load test with multiple concurrent users
5. Test on mobile devices
6. Verify accessibility compliance
