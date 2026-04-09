# Document Actions Guide

## 📄 Complete Functionality for View, Share, and Delete Buttons

All document action buttons are now fully functional with complete implementations.

---

## 🔵 VIEW Button

### What It Does
Opens a detailed modal showing all document information and metadata.

### Features
- **Document Details Display**:
  - Filename
  - Category/Type
  - File size
  - Upload date
  - Privacy score (0-100)
  - Verification status
  - Blockchain security status

- **Quick Actions**:
  - Share button (opens share dialog)
  - Download button (prepares file download)
  - Close button

### How to Use
1. Click the **"View"** button on any document card
2. Modal opens with complete document details
3. Review all information
4. Use quick action buttons or close

### Technical Implementation
```javascript
async function viewDocument(id) {
    // Fetches document details from API
    // Creates modal with formatted information
    // Displays metadata and status
    // Provides quick action buttons
}
```

### API Endpoint
```
GET /api/documents/{id}
Authorization: Bearer {token}
```

---

## 🟢 SHARE Button

### What It Does
Creates a secure, time-limited share link for the document with customizable access controls.

### Features

#### Access Controls
- **Access Limit**: Set maximum number of times link can be accessed (1-100)
- **Expiration**: Choose when link expires
  - 24 hours
  - 3 days
  - 1 week
  - 30 days

#### Security Options
- **Require OTP**: Force OTP verification before access (recommended)
- **Allow Download**: Enable/disable file download
- **Auto-mask**: Automatically mask sensitive data in document

### How to Use

#### Method 1: From Document Card
1. Click **"Share"** button on document card
2. Share modal opens
3. Configure settings:
   - Set access limit (default: 10)
   - Choose expiration time
   - Toggle security options
4. Click **"Generate Link"**
5. Copy the generated link
6. Share link with recipient

#### Method 2: From View Modal
1. Click **"View"** on document
2. Click **"Share"** in the view modal
3. Follow same steps as above

#### Method 3: From Context Menu
1. Click **"⋯"** menu on document card
2. Select **"Share Document"**
3. Follow configuration steps

### Generated Link Format
```
https://datavault.secure/s/abc123def456
```

### Share Link Features
- Unique token for each share
- Tracks access count
- Expires automatically
- Can be revoked anytime
- OTP protection (if enabled)

### Technical Implementation
```javascript
async function shareDocument(documentId) {
    // Opens share configuration modal
    // Collects user preferences
    // Calls API to create share
    // Displays generated link
}

async function generateShareLinkForDoc(documentId) {
    // Validates settings
    // Creates share via API
    // Returns shareable URL
}
```

### API Endpoint
```
POST /api/shares/
Authorization: Bearer {token}
Body: {
    document_id: "uuid",
    access_limit: 10,
    expires_in_hours: 24,
    require_otp: true,
    allow_download: false,
    auto_mask: true
}
```

### Response
```json
{
    "message": "Share link created successfully",
    "share": {
        "id": "uuid",
        "share_url": "https://datavault.secure/s/token",
        "expires_at": "2024-03-19T12:00:00Z",
        "access_count": 0,
        "max_access": 10,
        "status": "active"
    }
}
```

---

## 🔴 DELETE Button

### What It Does
Permanently removes the document from the system (both database and file storage).

### Features
- **Confirmation Dialog**: Prevents accidental deletion
- **Permanent Removal**: Deletes from database and disk
- **Automatic Refresh**: Updates document list after deletion
- **Stats Update**: Recalculates document count

### How to Use

#### Method 1: From Context Menu
1. Click **"⋯"** menu on document card
2. Select **"Delete Document"**
3. Confirm deletion in dialog
4. Document is removed

#### Method 2: Direct Function Call
```javascript
deleteDocument('document-id')
```

### Confirmation Dialog
```
Are you sure you want to delete this document?
This action cannot be undone.

[Cancel] [OK]
```

### What Gets Deleted
- ✅ Document record from PostgreSQL database
- ✅ Physical file from disk (`backend/uploads/`)
- ✅ Associated share links
- ✅ Access logs (retained for audit)

### Technical Implementation
```javascript
async function deleteDocument(id) {
    // Shows confirmation dialog
    // Calls delete API endpoint
    // Removes file from storage
    // Deletes database record
    // Refreshes document list
    // Updates statistics
}
```

### API Endpoint
```
DELETE /api/documents/{id}
Authorization: Bearer {token}
```

### Response
```json
{
    "message": "Document deleted successfully"
}
```

---

## 📋 Context Menu (⋯ Button)

### What It Does
Opens a context menu with all available document actions.

### Menu Options

1. **👁️ View Details**
   - Opens document details modal
   - Shows all metadata

2. **🔗 Share Document**
   - Opens share configuration
   - Creates shareable link

3. **⬇️ Download**
   - Prepares file for download
   - Saves to local device

4. **🗑️ Delete Document** (Red)
   - Permanently removes document
   - Requires confirmation

### How to Use
1. Click **"⋯"** button on any document card
2. Menu appears near cursor
3. Click any option
4. Menu closes automatically

### Technical Implementation
```javascript
function showDocumentMenu(id) {
    // Creates context menu element
    // Positions near cursor
    // Adds click handlers
    // Auto-closes on outside click
}
```

---

## 🎨 Visual Feedback

### Button States

#### View Button (Purple)
- Default: Purple background
- Hover: Lighter purple
- Active: Darker purple
- Icon: 👁️

#### Share Button (Cyan)
- Default: Cyan background
- Hover: Lighter cyan
- Active: Darker cyan
- Icon: 🔗

#### Delete Button (Red)
- Default: Red background
- Hover: Lighter red
- Active: Darker red
- Icon: 🗑️

### Notifications

#### Success Messages
- ✅ "Document deleted successfully!"
- ✅ "Share link created successfully!"
- ✅ "Link copied to clipboard!"

#### Info Messages
- ℹ️ "Loading document..."
- ℹ️ "Generating share link..."
- ℹ️ "Deleting document..."

#### Error Messages
- ❌ "Failed to load document: [reason]"
- ❌ "Failed to create share: [reason]"
- ❌ "Failed to delete document: [reason]"

---

## 🔄 Workflow Examples

### Example 1: View and Share
```
1. User clicks "View" on document
2. Modal opens with details
3. User clicks "Share" in modal
4. Share dialog opens
5. User configures settings
6. Clicks "Generate Link"
7. Link is created and displayed
8. User clicks "Copy"
9. Link copied to clipboard
10. User shares link via email/chat
```

### Example 2: Quick Delete
```
1. User clicks "⋯" menu
2. Selects "Delete Document"
3. Confirmation dialog appears
4. User clicks "OK"
5. Document is deleted
6. List refreshes automatically
7. Success notification shown
```

### Example 3: Share with Security
```
1. Click "Share" on document
2. Set access limit: 5
3. Set expiration: 24 hours
4. Enable "Require OTP"
5. Enable "Auto-mask"
6. Disable "Allow Download"
7. Generate link
8. Share with recipient
9. Recipient needs OTP to access
10. Link expires after 24 hours
```

---

## 🔐 Security Features

### View Action
- ✅ Requires authentication
- ✅ User can only view own documents
- ✅ No sensitive data exposed

### Share Action
- ✅ Unique token per share
- ✅ Optional OTP protection
- ✅ Time-limited access
- ✅ Access count tracking
- ✅ Auto-masking of sensitive data
- ✅ Revocable links

### Delete Action
- ✅ Confirmation required
- ✅ Permanent removal
- ✅ Audit trail maintained
- ✅ User can only delete own documents

---

## 📱 Responsive Design

All modals and menus are:
- ✅ Mobile-friendly
- ✅ Touch-optimized
- ✅ Keyboard accessible
- ✅ Screen reader compatible

---

## 🧪 Testing

### Test View Button
```javascript
// Open browser console
viewDocument('document-id-here')
```

### Test Share Button
```javascript
// Open browser console
shareDocument('document-id-here')
```

### Test Delete Button
```javascript
// Open browser console
deleteDocument('document-id-here')
```

---

## 🐛 Troubleshooting

### Buttons Not Working?

1. **Clear Browser Cache**
   ```
   Ctrl + Shift + Delete
   Clear cached files
   Hard refresh: Ctrl + F5
   ```

2. **Check Console for Errors**
   ```
   F12 → Console tab
   Look for JavaScript errors
   ```

3. **Verify Authentication**
   ```
   Check if logged in
   Token should be in localStorage
   ```

4. **Check API Connection**
   ```
   Test: http://localhost:8001/health
   Should return status: healthy
   ```

### Common Issues

**"Document not found"**
- Document may have been deleted
- Refresh the page
- Check if still in database

**"Failed to create share"**
- Check backend is running
- Verify API connection
- Check browser console

**"Delete failed"**
- May not have permission
- Document may be shared
- Check backend logs

---

## 📊 Database Impact

### View Action
- No database changes
- Read-only operation
- Access logged

### Share Action
- Creates new share record
- Generates unique token
- Sets expiration time
- Tracks access count

### Delete Action
- Removes document record
- Deletes file from disk
- Removes associated shares
- Maintains access logs (audit)

---

## 🎯 Best Practices

### When to Use View
- Review document details
- Check verification status
- Verify blockchain security
- Before sharing or deleting

### When to Use Share
- Collaborate with others
- Temporary access needed
- Controlled document access
- Time-limited sharing

### When to Use Delete
- Document no longer needed
- Duplicate files
- Outdated information
- Privacy concerns

---

## 🔄 Future Enhancements

### Planned Features
- [ ] Bulk operations (select multiple)
- [ ] Document preview in modal
- [ ] Edit document metadata
- [ ] Move to folders
- [ ] Tag management
- [ ] Advanced search
- [ ] Export options
- [ ] Version history

---

**Status**: ✅ FULLY IMPLEMENTED
**Version**: 3.0
**Last Updated**: March 18, 2026
**Tested**: All features working
