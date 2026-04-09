# Testing Access Tracking System

## Quick Test Guide

### Prerequisites
- Backend server running on port 8001
- Frontend accessible
- User account created and logged in

### Test Steps

#### 1. Create a Share Link
1. Login to DataVault
2. Go to "My Documents" page
3. Upload a document (if not already uploaded)
4. Click "Share" button on any document
5. Configure share settings:
   - Set expiry (e.g., 7 days)
   - Set access limit (e.g., 10 views)
   - Enable/disable OTP
6. Click "Create Share Link"
7. Copy the generated link

#### 2. Access the Share Link
1. Open the share link in:
   - Same browser (incognito mode)
   - Different browser
   - Different device (mobile/tablet)
2. Complete OTP verification if enabled
3. View the document
4. Repeat from different locations/devices if possible

#### 3. View Access Logs
1. Go to "Shared Links" page
2. Find your shared document
3. Click "View Logs" button
4. Verify the following information is displayed:
   - **Summary Statistics**:
     - Total accesses
     - Successful accesses
     - Unique visitors
   - **Individual Log Entries**:
     - IP address
     - Location (city, country)
     - Device info (browser, OS)
     - Timestamp
     - Status (success/attempt)
     - Risk level

### Expected Results

#### For Localhost Testing
```
IP Address: 127.0.0.1 or ::1
Location: Local, Local
Device: Chrome on Windows (or your actual browser/OS)
Status: success
Risk Level: low
```

#### For Production/Remote Testing
```
IP Address: 203.192.xxx.xxx (actual IP)
Location: Chennai, India (actual location)
Device: Chrome on Windows
Status: success
Risk Level: low
```

### Test Scenarios

#### Scenario 1: Successful Access
- Access share link with valid token
- Complete OTP if required
- **Expected**: Log entry with status "success"

#### Scenario 2: Multiple Accesses
- Access same link multiple times
- **Expected**: Multiple log entries with same/different IPs

#### Scenario 3: Different Devices
- Access from desktop, mobile, tablet
- **Expected**: Different device types in logs

#### Scenario 4: Different Locations
- Use VPN or access from different networks
- **Expected**: Different locations in logs

#### Scenario 5: Failed Access
- Try accessing expired link
- Try accessing revoked link
- **Expected**: Log entries with status "attempt" or "failed"

### Verification Checklist

- [ ] Share link created successfully
- [ ] Access logs endpoint returns data
- [ ] IP address captured correctly
- [ ] Geolocation data present (or "Local" for localhost)
- [ ] Device info parsed correctly
- [ ] Timestamp accurate
- [ ] Status reflects actual outcome
- [ ] Unique visitor count accurate
- [ ] UI displays logs beautifully
- [ ] Modal scrolls for many logs
- [ ] Color coding works (green=success, yellow=attempt)

### Troubleshooting

#### No logs showing
- Check if share was actually accessed
- Verify share_token matches
- Check browser console for errors
- Verify backend is running

#### Location shows "Unknown"
- Normal for localhost (127.0.0.1)
- Check internet connection for ip-api.com
- Verify no firewall blocking external requests

#### Device info incomplete
- Some user agents may not parse fully
- This is expected behavior
- Core functionality still works

### API Testing (Optional)

#### Using curl
```bash
# Get access logs for a share
curl -X GET "http://localhost:8001/api/shares/{share_token}/logs" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"
```

#### Expected Response
```json
{
  "share_token": "abc123...",
  "document_name": "document.pdf",
  "total_accesses": 5,
  "successful_accesses": 4,
  "unique_visitors": 3,
  "logs": [
    {
      "id": "log-id",
      "ip_address": "192.168.1.1",
      "location": {
        "city": "Chennai",
        "country": "India",
        "region": "Tamil Nadu",
        "lat": 13.0827,
        "lon": 80.2707
      },
      "device_info": {
        "browser": "Chrome",
        "os": "Windows",
        "device": "Desktop",
        "user_agent": "Mozilla/5.0..."
      },
      "timestamp": "2026-03-21T19:30:00",
      "status": "success",
      "risk_level": "low"
    }
  ]
}
```

### Demo Script

**For Presentation:**

1. **Show Share Creation**
   - "First, I'll create a secure share link for this document"
   - Create share with settings

2. **Access the Link**
   - "Now I'll access this link as if I'm a recipient"
   - Open in incognito/different browser
   - Complete the access flow

3. **View Access Logs**
   - "Back in my dashboard, I can see exactly who accessed my document"
   - Click "View Logs"
   - Point out key information:
     - "Here's the IP address"
     - "The system automatically detected the location"
     - "And captured the device and browser information"
     - "All with precise timestamps"

4. **Highlight Features**
   - "This gives me complete visibility"
   - "I can track unique visitors"
   - "Monitor for suspicious activity"
   - "And maintain full audit trails for compliance"

### Success Criteria

✅ All access attempts are logged
✅ IP addresses captured accurately
✅ Geolocation data retrieved (when available)
✅ Device information parsed correctly
✅ Timestamps are accurate
✅ Status reflects actual outcomes
✅ UI displays logs clearly
✅ Statistics calculated correctly
✅ Only owner can view logs
✅ System handles errors gracefully

## Status: Ready for Testing ✅
