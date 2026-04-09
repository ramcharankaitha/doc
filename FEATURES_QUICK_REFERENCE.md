# Quick Reference - Enhanced Features

## 🛡️ Admin Panel

### Keyboard Shortcuts
- `Ctrl/Cmd + R` - Refresh data
- `Ctrl/Cmd + F` - Focus search
- `Esc` - Clear search

### Console Commands
```javascript
AdminPanel.refresh()           // Refresh all data
AdminPanel.exportLogs()        // Export logs to CSV
AdminPanel.bulkDismiss()       // Dismiss all alerts
AdminPanel.toggleAutoRefresh() // Toggle auto-refresh
AdminPanel.getStats()          // Get statistics
```

### Features
✅ Real-time alert filtering (HIGH/MEDIUM/LOW)
✅ Multi-field log search
✅ CSV export for logs
✅ Bulk alert dismissal
✅ Advanced user locking with reasons
✅ Custom voice call messages
✅ Auto-refresh (30s interval)

---

## 👑 Super Admin Panel

### Keyboard Shortcuts
- `Ctrl/Cmd + R` - Refresh data
- `Ctrl/Cmd + H` - System health check
- `Ctrl/Cmd + E` - Export report

### Console Commands
```javascript
SuperAdminPanel.refresh()         // Refresh all data
SuperAdminPanel.addAdmin()        // Add admin (advanced)
SuperAdminPanel.bulkActions()     // Bulk operations menu
SuperAdminPanel.exportAdmins()    // Export admins to CSV
SuperAdminPanel.checkHealth()     // System health check
SuperAdminPanel.generateReport()  // Generate platform report
SuperAdminPanel.toggleAutoRefresh() // Toggle auto-refresh
SuperAdminPanel.getSummary()      // Get platform summary
```

### Features
✅ Advanced admin creation with roles
✅ Bulk admin operations
✅ CSV export for admins
✅ AI configuration presets (High/Balanced/Low)
✅ System health monitoring
✅ Platform report generation
✅ Auto-refresh (60s interval)

---

## 🎯 AI Configuration Presets

### High Security
- Sensitivity: 90% | Threshold: 50 | Duration: 12h | Lock: 70

### Balanced (Recommended)
- Sensitivity: 75% | Threshold: 65 | Duration: 24h | Lock: 85

### Low Security
- Sensitivity: 50% | Threshold: 80 | Duration: 72h | Lock: 95

---

## 📊 Quick Actions

### Admin Panel
1. Filter alerts → Select risk level
2. Search logs → Type in search box
3. Export data → Click "Export CSV"
4. Dismiss alerts → `AdminPanel.bulkDismiss()`
5. Lock user → Click lock button

### Super Admin Panel
1. Add admin → Click "+ Add Admin"
2. Health check → `Ctrl + H`
3. Export report → `Ctrl + E`
4. Configure AI → Click "Save Changes"
5. Bulk actions → `SuperAdminPanel.bulkActions()`

---

## 🔧 Troubleshooting

**Search not working?**
→ Check console, ensure backend running

**Export fails?**
→ Check popup blocker

**Auto-refresh stopped?**
→ Toggle twice: `Panel.toggleAutoRefresh()`

**Shortcuts not working?**
→ Click page, avoid input fields

---

## 📱 Access

**Admin Panel**: `frontend/admin.html`
**Super Admin Panel**: `frontend/superadmin.html`

**Admin Login**: admin@datavault.com / Admin2024!
**Super Admin Login**: superadmin@datavault.com / SuperAdmin2024!

---

**Full Guide**: See `ENHANCED_FEATURES_GUIDE.md`
