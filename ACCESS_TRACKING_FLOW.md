# Access Tracking System - Flow Diagram

## System Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                     ACCESS TRACKING SYSTEM                       │
└─────────────────────────────────────────────────────────────────┘

┌──────────────┐         ┌──────────────┐         ┌──────────────┐
│   Frontend   │────────▶│   Backend    │────────▶│   Database   │
│  (Browser)   │         │   (FastAPI)  │         │ (PostgreSQL) │
└──────────────┘         └──────────────┘         └──────────────┘
       │                        │                         │
       │                        │                         │
       ▼                        ▼                         ▼
  User Actions          Request Processing          Data Storage
```

## Access Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    SHARE ACCESS FLOW                             │
└─────────────────────────────────────────────────────────────────┘

1. User Clicks Share Link
   │
   ▼
2. Request Sent to Backend
   │
   ├─▶ Extract IP Address
   │   └─▶ Check X-Forwarded-For header
   │       └─▶ Fallback to request.client.host
   │
   ├─▶ Get Geolocation
   │   └─▶ Call ip-api.com/json/{ip}
   │       └─▶ Parse city, country, region, lat, lon
   │           └─▶ Fallback to "Unknown" on error
   │
   ├─▶ Parse Device Info
   │   └─▶ Extract User-Agent header
   │       └─▶ Detect browser (Chrome, Firefox, Safari, Edge)
   │       └─▶ Detect OS (Windows, macOS, Linux, Android, iOS)
   │       └─▶ Detect device type (Desktop, Mobile, Tablet)
   │
   ▼
3. Create Access Log Entry
   │
   ├─▶ Store in database:
   │   ├─ ip_address
   │   ├─ location (JSON)
   │   ├─ device_info (JSON)
   │   ├─ timestamp
   │   ├─ action (share_access_{token})
   │   └─ risk_level
   │
   ▼
4. Validate Share Link
   │
   ├─▶ Check if exists
   ├─▶ Check if active
   ├─▶ Check if expired
   ├─▶ Check access limit
   └─▶ Check OTP (if required)
   │
   ▼
5. Update Log Status
   │
   ├─▶ Success: action = "share_access_{token}_success"
   └─▶ Failure: action = "share_access_{token}_failed"
   │
   ▼
6. Return Document or Error
```

## View Logs Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    VIEW LOGS FLOW                                │
└─────────────────────────────────────────────────────────────────┘

1. User Clicks "View Logs" Button
   │
   ▼
2. Frontend Calls API
   │
   └─▶ GET /api/shares/{share_token}/logs
       └─▶ Authorization: Bearer {token}
   │
   ▼
3. Backend Validates Request
   │
   ├─▶ Verify user authentication
   ├─▶ Check share ownership
   └─▶ Verify share exists
   │
   ▼
4. Query Access Logs
   │
   ├─▶ Filter by document_id
   ├─▶ Filter by share_token in action
   └─▶ Order by created_at DESC
   │
   ▼
5. Calculate Statistics
   │
   ├─▶ Total accesses: count(logs)
   ├─▶ Successful: count(logs with "success")
   └─▶ Unique visitors: count(distinct ip_address)
   │
   ▼
6. Format Response
   │
   └─▶ Return JSON with:
       ├─ share_token
       ├─ document_name
       ├─ total_accesses
       ├─ successful_accesses
       ├─ unique_visitors
       └─ logs[] (array of log entries)
   │
   ▼
7. Frontend Displays Modal
   │
   ├─▶ Show summary statistics
   ├─▶ Render log entries
   ├─▶ Color-code status
   └─▶ Format timestamps
```

## Data Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                      DATA FLOW                                   │
└─────────────────────────────────────────────────────────────────┘

Request Headers                  External API              Database
─────────────────               ──────────────            ──────────
│                                    │                         │
├─ X-Forwarded-For: 203.192.45.67  │                         │
├─ User-Agent: Mozilla/5.0...       │                         │
│                                    │                         │
│                                    │                         │
▼                                    ▼                         │
Extract IP ──────────────────▶ ip-api.com                     │
203.192.45.67                  /json/203.192.45.67            │
                                    │                         │
                                    ▼                         │
                               Response:                      │
                               {                              │
                                 "city": "Chennai",           │
                                 "country": "India",          │
                                 "region": "Tamil Nadu",      │
                                 "lat": 13.0827,              │
                                 "lon": 80.2707               │
                               }                              │
                                    │                         │
                                    ▼                         │
Parse User-Agent                                              │
Mozilla/5.0 (Windows NT 10.0...)                             │
│                                                             │
├─▶ Browser: Chrome                                          │
├─▶ OS: Windows                                              │
└─▶ Device: Desktop                                          │
                                                              │
                                                              ▼
                                                         Store in DB:
                                                         ────────────
                                                         AccessLog {
                                                           ip_address: "203.192.45.67"
                                                           location: {
                                                             city: "Chennai",
                                                             country: "India",
                                                             region: "Tamil Nadu",
                                                             lat: 13.0827,
                                                             lon: 80.2707
                                                           }
                                                           device_info: {
                                                             browser: "Chrome",
                                                             os: "Windows",
                                                             device: "Desktop",
                                                             user_agent: "Mozilla/5.0..."
                                                           }
                                                           timestamp: "2026-03-21T19:30:00"
                                                           status: "success"
                                                           risk_level: "low"
                                                         }
```

## Component Interaction

```
┌─────────────────────────────────────────────────────────────────┐
│                  COMPONENT INTERACTION                           │
└─────────────────────────────────────────────────────────────────┘

Frontend Components:
┌──────────────────────────────────────────────────────────────┐
│  shared-links.html                                           │
│  ├─ Share Link Cards                                         │
│  │  └─ [View Logs] Button ──────────────┐                   │
│  │                                       │                   │
│  └─ viewAccessLogs(shareToken) ◀────────┘                   │
│     │                                                        │
│     └─▶ Calls SharesAPI.getAccessLogs()                     │
│         │                                                    │
│         └─▶ Displays Modal with Logs                        │
└──────────────────────────────────────────────────────────────┘
                          │
                          │ HTTP GET Request
                          │
                          ▼
Backend Components:
┌──────────────────────────────────────────────────────────────┐
│  shares.py                                                   │
│  ├─ get_share_access_logs(share_token)                      │
│  │  ├─ Verify ownership                                     │
│  │  ├─ Query AccessLog table                                │
│  │  ├─ Calculate statistics                                 │
│  │  └─ Return formatted response                            │
│  │                                                           │
│  ├─ access_share(share_token)                               │
│  │  ├─ get_client_ip(request)                               │
│  │  ├─ get_geolocation(ip)                                  │
│  │  ├─ get_device_info(request)                             │
│  │  ├─ Create AccessLog entry                               │
│  │  └─ Validate and process access                          │
│  │                                                           │
│  └─ Helper Functions:                                        │
│     ├─ get_client_ip()                                       │
│     ├─ get_geolocation()                                     │
│     └─ get_device_info()                                     │
└──────────────────────────────────────────────────────────────┘
                          │
                          │ Database Queries
                          │
                          ▼
Database:
┌──────────────────────────────────────────────────────────────┐
│  Tables                                                      │
│  ├─ shares                                                   │
│  │  ├─ id, share_token, document_id, user_id               │
│  │  └─ access_count, expires_at, is_active                 │
│  │                                                           │
│  ├─ access_logs                                              │
│  │  ├─ id, user_id, document_id, action                    │
│  │  ├─ ip_address, location (JSON)                         │
│  │  ├─ device_info (JSON), risk_level                      │
│  │  └─ created_at                                           │
│  │                                                           │
│  └─ documents                                                │
│     └─ id, file_name, user_id                               │
└──────────────────────────────────────────────────────────────┘
```

## Security Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECURITY FLOW                                 │
└─────────────────────────────────────────────────────────────────┘

1. Request Received
   │
   ▼
2. Authentication Check
   │
   ├─▶ Extract Bearer token
   ├─▶ Verify JWT signature
   ├─▶ Check token expiry
   └─▶ Get user_id from token
   │
   ▼
3. Authorization Check
   │
   ├─▶ Query share by share_token
   ├─▶ Verify share.user_id == current_user.user_id
   └─▶ Reject if not owner
   │
   ▼
4. Data Access
   │
   ├─▶ Only owner's logs returned
   ├─▶ No cross-user data leakage
   └─▶ Proper error messages
   │
   ▼
5. Response
   │
   └─▶ Return authorized data only
```

## Error Handling Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                  ERROR HANDLING FLOW                             │
└─────────────────────────────────────────────────────────────────┘

Geolocation Lookup
│
├─▶ Try: requests.get(ip-api.com)
│   │
│   ├─▶ Success: Return location data
│   │
│   └─▶ Failure:
│       ├─ Timeout (3 seconds)
│       ├─ Network error
│       ├─ Invalid response
│       └─▶ Return: {city: "Unknown", country: "Unknown"}
│
Share Access
│
├─▶ Try: Validate share
│   │
│   ├─▶ Not found: 404 "Share link not found"
│   ├─▶ Revoked: 403 "Share link has been revoked"
│   ├─▶ Expired: 403 "Share link has expired"
│   ├─▶ Limit reached: 403 "Access limit reached"
│   ├─▶ Invalid OTP: 401 "Invalid OTP"
│   └─▶ Success: Return document
│
View Logs
│
├─▶ Try: Get logs
│   │
│   ├─▶ Not authenticated: 401 "Unauthorized"
│   ├─▶ Not owner: 404 "Share not found"
│   ├─▶ Database error: 500 "Internal server error"
│   └─▶ Success: Return logs
```

## Performance Optimization

```
┌─────────────────────────────────────────────────────────────────┐
│                PERFORMANCE OPTIMIZATION                          │
└─────────────────────────────────────────────────────────────────┘

Geolocation Lookup:
├─ Timeout: 3 seconds (prevents hanging)
├─ Async: Non-blocking request
└─ Future: Consider caching by IP

Database Queries:
├─ Indexed: share_token, document_id
├─ Filtered: Specific share only
└─ Ordered: DESC by created_at

Response Size:
├─ Paginated: Can add limit/offset
├─ Filtered: Only relevant fields
└─ Compressed: JSON response

Frontend:
├─ Lazy loading: Logs loaded on demand
├─ Cached: API responses cached
└─ Optimized: Minimal re-renders
```

## Monitoring & Analytics

```
┌─────────────────────────────────────────────────────────────────┐
│                MONITORING & ANALYTICS                            │
└─────────────────────────────────────────────────────────────────┘

Metrics Tracked:
├─ Total accesses per share
├─ Successful vs failed attempts
├─ Unique visitors (by IP)
├─ Geographic distribution
├─ Device/browser breakdown
└─ Access patterns over time

Alerts (Future):
├─ Multiple failed attempts
├─ Access from unusual location
├─ Rapid successive accesses
├─ High-risk IP addresses
└─ Access outside business hours

Reports (Future):
├─ Daily access summary
├─ Weekly analytics
├─ Monthly compliance report
└─ Custom date ranges
```

---

## Visual Summary

```
┌─────────────────────────────────────────────────────────────────┐
│                    SYSTEM OVERVIEW                               │
└─────────────────────────────────────────────────────────────────┘

User Actions:
  1. Create Share Link
  2. Access Share Link
  3. View Access Logs

System Captures:
  • IP Address (with proxy support)
  • Geolocation (city, country, region)
  • Device Info (browser, OS, device type)
  • Timestamp (precise to millisecond)
  • Status (success/attempt/failed)
  • Risk Level (low/medium/high)

Benefits:
  ✓ Complete visibility
  ✓ Security monitoring
  ✓ Compliance ready
  ✓ Analytics insights
  ✓ Threat detection
  ✓ Audit trails
```

---

**This flow diagram provides a complete visual understanding of the Access Tracking System architecture and operation.**
