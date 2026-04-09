# 🎯 Quick Button Functions Summary

## Document Card Buttons

```
┌─────────────────────────────────────────────────────┐
│  📄 Document Name                                   │
│  Uploaded: 2024-03-18                               │
│  Size: 2.4 MB                                       │
│                                                     │
│  [View] [Share] [⋯]                                 │
└─────────────────────────────────────────────────────┘
```

---

## 🔵 VIEW Button

**What it does**: Opens detailed document information

**Click to see**:
- ✅ Full filename
- ✅ Document category
- ✅ File size
- ✅ Upload date
- ✅ Privacy score (0-100)
- ✅ Verification status
- ✅ Blockchain security
- ✅ Quick action buttons

**Example**:
```
┌──────────────────────────────────────┐
│  📄 Document Details                 │
├──────────────────────────────────────┤
│  Filename: passport_scan.pdf         │
│  Category: Passport                  │
│  Size: 2.4 MB                        │
│  Uploaded: Mar 18, 2024 10:30 AM     │
│  Privacy Score: 95/100               │
│  Status: ✓ Verified                  │
│  Blockchain: ⛓ Secured               │
├──────────────────────────────────────┤
│  [🔗 Share] [⬇️ Download] [Close]    │
└──────────────────────────────────────┘
```

---

## 🟢 SHARE Button

**What it does**: Creates secure shareable link

**Configuration options**:
1. **Access Limit**: How many times link can be used (1-100)
2. **Expiration**: When link expires (24h, 3d, 1w, 30d)
3. **Require OTP**: Force OTP verification ✅ Recommended
4. **Allow Download**: Let recipient download file
5. **Auto-mask**: Hide sensitive data automatically

**Generated link**:
```
https://datavault.secure/s/abc123def456
```

**Example workflow**:
```
1. Click "Share" button
   ↓
2. Configure settings:
   - Access limit: 10 times
   - Expires: 24 hours
   - Require OTP: ✓ ON
   - Allow download: ✗ OFF
   - Auto-mask: ✓ ON
   ↓
3. Click "Generate Link"
   ↓
4. Copy link
   ↓
5. Share with recipient
   ↓
6. Recipient needs OTP to access
   ↓
7. Link expires after 24 hours
```

**Security features**:
- 🔐 Unique token per share
- ⏰ Time-limited access
- 🔢 Access count tracking
- 🔑 Optional OTP protection
- 🎭 Auto-masking sensitive data
- ❌ Revocable anytime

---

## 🔴 DELETE Button

**What it does**: Permanently removes document

**Confirmation required**:
```
┌──────────────────────────────────────┐
│  ⚠️ Delete Document?                 │
├──────────────────────────────────────┤
│  Are you sure you want to delete     │
│  this document?                      │
│                                      │
│  This action cannot be undone.       │
├──────────────────────────────────────┤
│  [Cancel] [OK]                       │
└──────────────────────────────────────┘
```

**What gets deleted**:
- ✅ Document from database
- ✅ File from disk storage
- ✅ Associated share links
- ✅ Document metadata

**What's kept** (for audit):
- ✅ Access logs
- ✅ Upload history

---

## 📋 Context Menu (⋯ Button)

**What it does**: Shows all available actions

**Menu options**:
```
┌──────────────────────────┐
│  👁️ View Details         │
│  🔗 Share Document       │
│  ⬇️ Download             │
│  ─────────────────       │
│  🗑️ Delete Document      │
└──────────────────────────┘
```

**How to use**:
1. Click **⋯** on document card
2. Menu appears
3. Select action
4. Menu closes automatically

---

## 🎬 Complete User Flows

### Flow 1: View Document Details
```
User clicks "View"
    ↓
Modal opens with details
    ↓
User reviews information
    ↓
User clicks "Close" or outside modal
    ↓
Modal closes
```

### Flow 2: Share Document Securely
```
User clicks "Share"
    ↓
Share modal opens
    ↓
User sets:
  - Access limit: 5
  - Expires: 3 days
  - Require OTP: ON
  - Allow download: OFF
    ↓
User clicks "Generate Link"
    ↓
Link created: https://datavault.secure/s/xyz789
    ↓
User clicks "Copy"
    ↓
Link copied to clipboard
    ↓
User shares via email/chat
    ↓
Recipient clicks link
    ↓
OTP sent to recipient
    ↓
Recipient enters OTP
    ↓
Document accessed (count: 1/5)
    ↓
After 3 days: Link expires automatically
```

### Flow 3: Delete Document
```
User clicks "⋯" menu
    ↓
User selects "Delete Document"
    ↓
Confirmation dialog appears
    ↓
User clicks "OK"
    ↓
Document deleted from:
  - Database ✓
  - Disk storage ✓
  - Share links ✓
    ↓
Document list refreshes
    ↓
Success notification shown
    ↓
Stats updated (document count -1)
```

---

## 🎨 Visual States

### Button Colors

**View Button**:
- Color: Purple (#7B5CFF)
- Icon: 👁️
- Action: Opens modal

**Share Button**:
- Color: Cyan (#00F5C8)
- Icon: 🔗
- Action: Creates link

**Delete Button**:
- Color: Red (#FF4B6E)
- Icon: 🗑️
- Action: Removes document

### Hover Effects
```
Normal:    [View]
Hover:     [View] ← Lighter color
Active:    [View] ← Darker color
Disabled:  [View] ← Gray, no cursor
```

---

## 📱 Mobile Support

All buttons work on:
- ✅ Desktop (mouse click)
- ✅ Tablet (touch)
- ✅ Mobile (touch)
- ✅ Keyboard (Tab + Enter)

---

## ⚡ Quick Actions

### Keyboard Shortcuts (Future)
```
V - View document
S - Share document
D - Delete document
Esc - Close modal
```

### Right-Click Menu (Future)
```
Right-click on document card
    ↓
Context menu appears
    ↓
Select action
```

---

## 🔔 Notifications

### Success
- ✅ "Document deleted successfully!"
- ✅ "Share link created!"
- ✅ "Link copied to clipboard!"

### Info
- ℹ️ "Loading document..."
- ℹ️ "Generating share link..."
- ℹ️ "Preparing download..."

### Error
- ❌ "Failed to load document"
- ❌ "Failed to create share"
- ❌ "Delete failed"

---

## 🎯 When to Use Each Button

### Use VIEW when you want to:
- ✅ Check document details
- ✅ Verify upload status
- ✅ See privacy score
- ✅ Check blockchain security
- ✅ Quick share or download

### Use SHARE when you want to:
- ✅ Collaborate with others
- ✅ Give temporary access
- ✅ Control who sees document
- ✅ Set expiration time
- ✅ Track access count

### Use DELETE when you want to:
- ✅ Remove old documents
- ✅ Delete duplicates
- ✅ Free up storage
- ✅ Remove sensitive data
- ✅ Clean up account

---

## 🔒 Security Summary

| Button | Authentication | Confirmation | Reversible | Audit Log |
|--------|---------------|--------------|------------|-----------|
| View   | ✅ Required   | ❌ No        | N/A        | ✅ Yes    |
| Share  | ✅ Required   | ❌ No        | ✅ Yes*    | ✅ Yes    |
| Delete | ✅ Required   | ✅ Yes       | ❌ No      | ✅ Yes    |

*Share links can be revoked

---

## 📊 Database Operations

### View Button
```sql
SELECT * FROM documents WHERE id = ? AND user_id = ?
-- Read-only, no changes
```

### Share Button
```sql
INSERT INTO shares (document_id, share_token, expires_at, ...)
VALUES (?, ?, ?, ...)
-- Creates new share record
```

### Delete Button
```sql
DELETE FROM documents WHERE id = ? AND user_id = ?
-- Removes document record
-- Also deletes physical file
```

---

## 🎓 Tips & Best Practices

### For View Button
- 💡 Use before sharing to verify details
- 💡 Check privacy score regularly
- 💡 Verify blockchain status

### For Share Button
- 💡 Always enable "Require OTP" for sensitive docs
- 💡 Set shortest expiration time needed
- 💡 Limit access count appropriately
- 💡 Disable download for extra security
- 💡 Enable auto-mask for PII documents

### For Delete Button
- 💡 Review document before deleting
- 💡 Check if document is shared
- 💡 Download backup if needed
- 💡 Remember: deletion is permanent!

---

## 🚀 Getting Started

1. **Login** to dashboard
2. **Upload** a document
3. **Click View** to see details
4. **Click Share** to create link
5. **Click Delete** to remove (if needed)

**Test it now**: http://localhost:3000/dashboard.html

---

**All buttons are fully functional and ready to use!** 🎉
