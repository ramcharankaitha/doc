# 🔍 QR Code Troubleshooting Guide

## Issue: Can't Find QR Code Option

### Quick Fix Steps

#### 1. Clear Browser Cache
The most common issue is cached old version of the page.

**Chrome/Edge:**
```
1. Press Ctrl + Shift + Delete
2. Select "Cached images and files"
3. Click "Clear data"
4. Refresh page (Ctrl + F5)
```

**Firefox:**
```
1. Press Ctrl + Shift + Delete
2. Select "Cache"
3. Click "Clear Now"
4. Refresh page (Ctrl + F5)
```

**Quick Method (All Browsers):**
```
Press Ctrl + F5 (Hard Refresh)
or
Ctrl + Shift + R
```

#### 2. Test QR Code Functionality
1. Open `test_qr_code.html` in your browser
2. Click "Generate QR Code" button
3. If QR code appears → Library works, cache issue
4. If error appears → Check internet connection

#### 3. Verify File Updated
Check if `frontend/shared-links.html` contains:

```html
<script src="https://cdn.jsdelivr.net/npm/qrcodejs@1.0.0/qrcode.min.js"></script>
```

Should be around line 302.

#### 4. Check Button Text
Look for button with text: **"🔗 Share"**

If you see:
- ✅ "🔗 Share" → Correct, new version
- ❌ "Copy Link" → Old version, clear cache

### Step-by-Step Testing

#### Test 1: Open Shared Links Page
1. Go to `frontend/shared-links.html`
2. Login if needed
3. Look at any shared link card
4. Find the buttons at the bottom

#### Test 2: Check Button Layout
You should see 3 buttons:
- 📊 Logs
- 🔗 Share ← This one!
- 🗑️ Revoke

#### Test 3: Click Share Button
1. Click "🔗 Share" button
2. Modal should appear with 2 options:
   - 🔗 Copy Link
   - 📱 Generate QR Code

#### Test 4: Generate QR Code
1. Click "📱 Generate QR Code"
2. QR code should appear
3. Two buttons below:
   - 💾 Download
   - Close

### Common Issues & Solutions

#### Issue 1: Button Says "Copy Link" Instead of "Share"
**Cause:** Browser cache
**Solution:**
```
1. Press Ctrl + Shift + Delete
2. Clear cache
3. Press Ctrl + F5 to hard refresh
```

#### Issue 2: Modal Doesn't Appear
**Cause:** JavaScript error
**Solution:**
```
1. Press F12 to open DevTools
2. Go to Console tab
3. Look for errors (red text)
4. Share the error message
```

#### Issue 3: QR Code Doesn't Generate
**Cause:** Library not loaded
**Solution:**
```
1. Check internet connection
2. Open test_qr_code.html
3. If test works, clear cache on main page
4. If test fails, check firewall/antivirus
```

#### Issue 4: "QRCode is not defined" Error
**Cause:** CDN blocked or slow connection
**Solution:**
```
1. Check if CDN is accessible:
   https://cdn.jsdelivr.net/npm/qrcodejs@1.0.0/qrcode.min.js
2. Try different browser
3. Check firewall settings
```

### Browser Console Checks

#### Open Console
```
Press F12 → Console tab
```

#### Check if QRCode Library Loaded
Type in console:
```javascript
typeof QRCode
```

Expected result:
- ✅ "function" → Library loaded
- ❌ "undefined" → Library not loaded

#### Check if Function Exists
Type in console:
```javascript
typeof showShareOptions
```

Expected result:
- ✅ "function" → Function exists
- ❌ "undefined" → Old version, clear cache

### Manual Test

#### Test Share Options Function
1. Open shared-links.html
2. Press F12 → Console
3. Type:
```javascript
showShareOptions('https://test.com', 'Test Document')
```
4. Press Enter
5. Modal should appear

#### Test QR Code Function
1. In console, type:
```javascript
showQRCode('https://test.com', 'Test Document')
```
2. Press Enter
3. QR code should appear

### File Verification

#### Check File Modified Date
```bash
# Windows
dir frontend\shared-links.html

# Should show recent modification date
```

#### Check File Size
The updated file should be larger:
- Old version: ~15 KB
- New version: ~20 KB

#### Search for QR Code in File
```bash
# Windows PowerShell
Select-String -Path "frontend\shared-links.html" -Pattern "qrcodejs"

# Should return line with CDN link
```

### Network Issues

#### Check CDN Accessibility
Open in browser:
```
https://cdn.jsdelivr.net/npm/qrcodejs@1.0.0/qrcode.min.js
```

Should show JavaScript code.

If blocked:
1. Check firewall
2. Check antivirus
3. Try different network
4. Use mobile hotspot

### Alternative: Local QR Library

If CDN is blocked, download library locally:

1. Download from:
   https://cdn.jsdelivr.net/npm/qrcodejs@1.0.0/qrcode.min.js

2. Save as: `frontend/assets/js/qrcode.min.js`

3. Update shared-links.html:
```html
<!-- Replace CDN line with: -->
<script src="assets/js/qrcode.min.js"></script>
```

### Verification Checklist

- [ ] Cleared browser cache
- [ ] Hard refreshed page (Ctrl + F5)
- [ ] See "🔗 Share" button (not "Copy Link")
- [ ] test_qr_code.html works
- [ ] Console shows no errors
- [ ] typeof QRCode returns "function"
- [ ] typeof showShareOptions returns "function"
- [ ] CDN link accessible
- [ ] File modification date is recent

### Still Not Working?

#### Collect Debug Information

1. **Browser & Version:**
   - Chrome/Firefox/Edge/Safari
   - Version number

2. **Console Errors:**
   - Press F12 → Console
   - Copy any red error messages

3. **Network Tab:**
   - Press F12 → Network
   - Refresh page
   - Check if qrcode.min.js loads (green status)

4. **File Check:**
   ```bash
   # Check if file contains QR code
   findstr /C:"qrcodejs" frontend\shared-links.html
   ```

### Quick Test Commands

#### PowerShell
```powershell
# Check file updated
(Get-Item "frontend\shared-links.html").LastWriteTime

# Search for QR code
Select-String -Path "frontend\shared-links.html" -Pattern "showShareOptions"

# Count lines (should be ~700+)
(Get-Content "frontend\shared-links.html").Count
```

### Expected Behavior

#### When Working Correctly:

1. **Shared Links Page:**
   - Shows list of shared documents
   - Each has 3 buttons: Logs, Share, Revoke

2. **Click Share:**
   - Modal appears instantly
   - Shows document name
   - Two large option buttons
   - Cancel button at bottom

3. **Click Generate QR Code:**
   - Share modal closes
   - QR modal appears
   - QR code generates in ~100ms
   - Shows Download and Close buttons

4. **Click Download:**
   - PNG file downloads
   - Filename: DocumentName_QR.png
   - Success notification appears

### Screenshots of Expected UI

#### Share Options Modal:
```
┌─────────────────────────────────┐
│      Share Document             │
│                                 │
│      contract.pdf               │
│                                 │
│  ┌───────────────────────────┐ │
│  │ 🔗  Copy Link             │ │
│  │     Copy the share link   │ │
│  └───────────────────────────┘ │
│                                 │
│  ┌───────────────────────────┐ │
│  │ 📱  Generate QR Code      │ │
│  │     Create a scannable QR │ │
│  └───────────────────────────┘ │
│                                 │
│         [Cancel]                │
└─────────────────────────────────┘
```

#### QR Code Modal:
```
┌─────────────────────────────────┐
│         QR Code                 │
│                                 │
│      contract.pdf               │
│                                 │
│  ┌─────────────────────────┐   │
│  │                         │   │
│  │    [QR CODE IMAGE]      │   │
│  │                         │   │
│  └─────────────────────────┘   │
│                                 │
│   [💾 Download]   [Close]      │
└─────────────────────────────────┘
```

### Contact Support

If still not working after all steps:

1. Run test_qr_code.html
2. Take screenshot of result
3. Open browser console (F12)
4. Take screenshot of any errors
5. Check file modification date
6. Provide browser name and version

---

## Quick Fix Summary

**Most Common Solution:**
```
1. Press Ctrl + Shift + Delete
2. Clear cache
3. Press Ctrl + F5
4. Look for "🔗 Share" button
5. Click it
6. Choose "Generate QR Code"
```

**If that doesn't work:**
```
1. Open test_qr_code.html
2. Click "Generate QR Code"
3. If it works → Cache issue on main page
4. If it fails → Internet/CDN issue
```

**Status: Ready to Debug** ✅
