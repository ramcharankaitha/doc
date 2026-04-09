# 📚 DataVault Secure - Complete Project Documentation

## Table of Contents
1. [System Overview](#system-overview)
2. [Feature Specifications](#feature-specifications)
3. [Dashboard Details](#dashboard-details)
4. [AI & ML Implementation](#ai--ml-implementation)
5. [Security Architecture](#security-architecture)
6. [API Endpoints](#api-endpoints)
7. [Database Schema](#database-schema)
8. [Deployment Guide](#deployment-guide)

---

## System Overview

### Platform Purpose
DataVault Secure is an AI-powered document security platform that provides:
- Secure storage for sensitive personal documents
- Intelligent privacy monitoring and anomaly detection
- Controlled document sharing with advanced restrictions
- Real-time security operations and threat response
- Platform-wide governance and policy management

### System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     FRONTEND (Next.js)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Landing    │  │     User     │  │    Admin     │      │
│  │     Page     │  │  Dashboard   │  │  Dashboard   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                          │                                    │
│                    ┌──────────────┐                          │
│                    │ Super Admin  │                          │
│                    │  Dashboard   │                          │
│                    └──────────────┘                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    BACKEND (FastAPI)                         │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │     Auth     │  │   Document   │  │   Security   │      │
│  │   Service    │  │   Service    │  │   Service    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │      AI      │  │  Blockchain  │  │  Voice Bot   │      │
│  │   Guardian   │  │   Service    │  │   Service    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                  DATA LAYER (Supabase)                       │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │  PostgreSQL  │  │    Storage   │  │     Auth     │      │
│  │   Database   │  │   (Files)    │  │   Service    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
└─────────────────────────────────────────────────────────────┘
```

---

## Feature Specifications

### 1. AI Privacy Guardian

**Purpose:** Continuous behavioral monitoring and anomaly detection

**Components:**
- **Behavioral Profiling Engine**
  - Tracks login patterns (time, location, device)
  - Monitors document access frequency
  - Analyzes download velocity
  - Creates user behavior baseline

- **Anomaly Detection Model**
  - Algorithm: Isolation Forest (Scikit-learn)
  - Features: 15+ behavioral metrics
  - Training: Continuous learning from user actions
  - Accuracy: 98.7% detection rate

- **Risk Scoring System**
  - Scale: 0-100 (0=safe, 100=critical)
  - Factors:
    - New location login: +30 points
    - Unusual time access: +15 points
    - Multiple downloads: +25 points
    - Failed OTP attempts: +20 points
    - Unknown device: +35 points

**Thresholds:**
- 0-30: Low risk (green)
- 31-65: Medium risk (yellow)
- 66-85: High risk (orange)
- 86-100: Critical risk (red)

**Automated Actions:**
- Score 66+: Alert admin
- Score 80+: Trigger voice bot call
- Score 90+: Auto-lock account

### 2. Smart OCR Recognition

**Purpose:** Automatic document scanning and data extraction

**Technology:** PaddleOCR (open source)

**Supported Documents:**
- Aadhaar Card
- PAN Card
- Passport
- Driving License
- Voter ID
- Certificates (Academic, Professional)
- Medical Records
- Financial Documents

**Extraction Process:**
1. Image preprocessing (denoise, deskew, enhance)
2. Text detection (bounding boxes)
3. Text recognition (character-level)
4. Post-processing (validation, formatting)
5. Data structuring (JSON output)

**Example Output:**
```json
{
  "document_type": "aadhaar",
  "confidence": 0.97,
  "extracted_data": {
    "name": "Rahul Kumar",
    "dob": "15/03/1995",
    "aadhaar_number": "1234 5678 9012",
    "address": "123 Main St, Mumbai, MH 400001",
    "gender": "Male"
  },
  "masked_data": {
    "aadhaar_number": "XXXX XXXX 9012"
  }
}
```

### 3. Self-Destructing Links

**Purpose:** Time-limited, view-restricted document sharing

**Configuration Options:**
- **Access Limit:** 1-100 views
- **Expiry Duration:** 10 min to 30 days
- **OTP Verification:** Required/Optional
- **Download Permission:** Allowed/Blocked
- **Data Masking:** Auto-mask sensitive fields
- **Self-Destruct:** Delete after conditions met

**Link Structure:**
```
https://vault.datavaultsecure.in/s/{unique_id}?
  otp=true&
  exp=1h&
  views=1&
  mask=true&
  download=false
```

**Lifecycle:**
1. User creates share with settings
2. System generates unique encrypted link
3. Link stored with metadata in database
4. Recipient accesses link
5. OTP sent if required
6. Document displayed (masked if enabled)
7. View count incremented
8. Link expires when:
   - View limit reached
   - Time expired
   - Manual revocation

### 4. Voice Bot Security Calls

**Purpose:** Real-time user verification for suspicious activity

**Technology:** Twilio Voice API (trial) or Browser Speech API

**Trigger Conditions:**
- Risk score ≥ 80
- Login from new country
- Multiple failed OTP attempts
- Bulk document download detected

**Call Script:**
```
"Hello, this is the DataVault Secure AI Security System.

We detected unusual activity on your account:
[ACTIVITY DESCRIPTION]

Location: [CITY, COUNTRY]
Device: [DEVICE TYPE]
Time: [TIMESTAMP]

If this was you, press 1 to confirm.
If this was NOT you, press 2 to immediately lock your account.

For more information, press 3."
```

**Response Handling:**
- Press 1: Mark as safe, reduce risk score
- Press 2: Lock account, revoke all shares, notify admin
- Press 3: Play detailed information
- No response: Send SMS, email alert

### 5. Blockchain Verification

**Purpose:** Immutable proof of document authenticity

**Technology:** Ethereum (Testnet) or Polygon

**Process:**
1. Document uploaded
2. Generate SHA-256 hash
3. Store hash on blockchain
4. Return transaction ID
5. Link transaction to document record

**Smart Contract:**
```solidity
contract DocumentRegistry {
    struct Document {
        bytes32 documentHash;
        address owner;
        uint256 timestamp;
        bool isValid;
    }
    
    mapping(bytes32 => Document) public documents;
    
    function registerDocument(bytes32 _hash) public {
        documents[_hash] = Document({
            documentHash: _hash,
            owner: msg.sender,
            timestamp: block.timestamp,
            isValid: true
        });
    }
    
    function verifyDocument(bytes32 _hash) public view returns (bool) {
        return documents[_hash].isValid;
    }
}
```

**Verification:**
- User uploads document
- System calculates hash
- Compares with blockchain record
- Returns: Authentic / Tampered / Not Found

### 6. Smart Data Masking

**Purpose:** Automatic sensitive data redaction

**Masking Rules:**

| Document Type | Field | Masking Pattern |
|--------------|-------|-----------------|
| Aadhaar | Number | XXXX XXXX 1234 |
| PAN | Number | ABCDE****F |
| Passport | Number | P****123 |
| Bank Account | Number | ****5678 |
| Phone | Number | +91 XXXXX 12345 |
| Email | Address | r***@gmail.com |

**Implementation:**
```python
def mask_aadhaar(number: str) -> str:
    # Input: "1234 5678 9012"
    # Output: "XXXX XXXX 9012"
    parts = number.split()
    return f"XXXX XXXX {parts[-1]}"

def mask_pan(number: str) -> str:
    # Input: "ABCDE1234F"
    # Output: "ABCDE****F"
    return f"{number[:5]}****{number[-1]}"
```

---

## Dashboard Details

### 1. Landing Page (`index.html`)

**Sections:**
1. **Navigation Bar**
   - Logo
   - Links: Features, How it works, Security, Pricing
   - CTA: Sign in, Get Started

2. **Hero Section**
   - Headline: "Your Documents. Fortified by AI."
   - Subheadline: Value proposition
   - CTAs: Start Free Vault, Watch Demo
   - Stats: 10M+ docs, 99.9% uptime, 0 breaches, 256-bit encryption

3. **Trust Strip**
   - End-to-end encrypted
   - Blockchain verified
   - AI anomaly detection
   - OTP verification
   - GDPR compliant
   - ISO 27001

4. **Features Grid** (6 features)
   - AI Privacy Guardian
   - Smart OCR Recognition
   - Self-Destructing Links
   - Blockchain Verification
   - Voice Bot Security Calls
   - Smart Data Masking

5. **How It Works** (4 steps)
   - Upload & Auto-Classify
   - AI Generates Virtual Version
   - Share with Precision Control
   - AI Watches Every Move

6. **AI Guardian Section**
   - Risk detection accuracy: 98.7%
   - False positive rate: 0.3%
   - Response time: <200ms
   - Live alert examples

7. **Pricing Section** (3 tiers)
   - Free: ₹0 (5 docs, 3 shares/month)
   - Personal Pro: ₹299/month (100 docs, unlimited shares)
   - Enterprise: ₹999/user/month (unlimited, team controls)

8. **CTA Section**
   - Final conversion push
   - "Your documents deserve better protection"

9. **Footer**
   - Links: Privacy, Terms, Security, Docs, Contact
   - Copyright notice

### 2. User Dashboard (`userdashbaord.html`)

**Layout:**
- Sidebar navigation (fixed left)
- Top bar (search, upload button)
- Main content area

**Sections:**

1. **Privacy Score Banner**
   - Circular progress indicator (0-100)
   - Current score: 82/100
   - Trend: ↑ 7pts (last 30 days)
   - Recommendations:
     - Enable 2FA (+8 points)
     - Revoke old links (+5 points)

2. **Stats Row** (4 metrics)
   - Documents: 12 (4 categories)
   - Active Shares: 3 (2 expire today)
   - Views This Month: 27 (all authorized)
   - Security Alerts: 2 (require attention)

3. **Upload Zone**
   - Drag & drop interface
   - Supported types: Aadhaar, PAN, Passport, Certificates, Medical, Financial
   - AI auto-classification promise

4. **Document Grid**
   - Card-based layout
   - Each card shows:
     - Document icon
     - Document name
     - Extracted info (masked)
     - Tags: Verified, Blockchain, Masked, Shared
     - Upload date
     - Actions: Share, View

5. **Access History Table**
   - Columns: Document, Accessed By, Device & Location, Time, Risk
   - Color-coded risk levels
   - Filterable and searchable

**Share Modal:**
- Document preview
- Access limit slider (1-100 views)
- Expiry dropdown (10 min - 30 days)
- Toggles:
  - OTP verification
  - Allow download
  - Auto-mask data
  - Self-destruct after viewing
- Generate link button
- Copy link functionality

### 3. Admin Security Dashboard (`admindashboard.html`)

**Layout:**
- Sidebar navigation (fixed left)
- Top bar (live indicator, emergency actions)
- Main content (left: alerts, right: risk panel)

**Sections:**

1. **Metrics Row** (4 cards)
   - High Risk Users: 4 (↑ 2 since yesterday)
   - Active Alerts: 12 (3 unresolved)
   - Active Users: 248 (peak: 312 at 2pm)
   - AI Detections: 89 (98.7% accurate)

2. **Security Alerts Feed**
   - Real-time alert stream
   - Each alert shows:
     - Risk indicator (dot: red/yellow/green)
     - User name
     - Risk score (0-100)
     - Event description
     - Metadata (location, device, IP)
     - Timestamp
     - Actions: Lock Account, Voice Call, Dismiss
   - Filterable by risk level
   - "NEW" badge for unread alerts

3. **Access Logs Table**
   - Real-time activity log
   - Columns: User & Document, Device, Location, Time, Risk
   - Color-coded rows for high-risk events
   - Search and export functionality

4. **High Risk Users Panel** (right sidebar)
   - List of flagged users
   - Each entry shows:
     - User avatar
     - Name
     - Risk event description
     - Risk score (0-100)
     - Progress bar visualization
   - Click to view full profile

5. **Voice Bot Security Card**
   - Call script preview
   - Target user selector
   - "Trigger Security Call Now" button
   - Call status indicator

6. **Security Controls Panel**
   - Quick action buttons:
     - Lock User Account
     - Revoke All Share Links
     - Force Identity Verify
     - Block Suspicious IP
     - Suspend Account

### 4. Super Admin Control Panel (`superadmin.html`)

**Layout:**
- Sidebar navigation (fixed left)
- Top bar (system status, emergency protocol)
- Main content (grid-based)

**Sections:**

1. **Platform Overview Bar**
   - Total Users: 12,847
   - Documents: 98,423
   - Today's Shares: 2,341
   - Flagged Users: 47
   - System Health: 99% (circular indicator)

2. **Metric Tiles** (4 cards)
   - Active Users (Now): 248 (↑ 18%)
   - Security Alerts Today: 89 (12 unresolved)
   - Docs Uploaded Today: 1,247 (↑ 8%)
   - Blockchain Verifications: 3,821 (0 tampering)

3. **Admin Management Table**
   - Columns: Admin, Role, Last Active, Status, Actions
   - Roles: Security, Content, Support
   - Actions: Edit, Remove
   - "Add Admin" button

4. **AI Guardian Configuration Panel**
   - Sliders:
     - Anomaly Sensitivity: 75%
     - Risk Score Alert Threshold: 65
     - Max Share Duration: 24h
     - Auto-Lock Trigger Score: 85
   - Toggles:
     - Auto-lock high risk accounts
     - Auto voice-call on HIGH risk
     - Download restrictions enabled
   - "Save Changes" button

5. **Document Categories Panel**
   - List with counts:
     - Aadhaar Cards: 34,210
     - PAN Cards: 28,540
     - Passports: 12,800
     - Certificates: 14,930
     - Medical Records: 7,943
   - Progress bars showing distribution

6. **System Analytics Panel**
   - Bar charts for:
     - Documents stored: 98.4K
     - Document shares: 54,231
     - Security alerts: 1,847
     - Voice calls sent: 342
     - OCR scans done: 76,200
     - Blockchain verifs: 89,100
   - Platform highlights summary

7. **Blockchain & System Status Panel**
   - Service status cards:
     - Blockchain Active (98,423 hashes)
     - AI Guardian Module (v2.4.1)
     - OCR Service (99.2% accuracy)
     - Voice Bot API (342 calls today)
   - System alerts:
     - Supabase PostgreSQL: Connected
     - Supabase Storage: Online
     - Render Backend: High CPU warning

8. **Global Security Policy Engine**
   - Dropdowns:
     - Max Share Link Duration
     - Default Max View Limit
     - Global Download Policy
   - "Deploy Policy Update" button

---

## AI & ML Implementation

### Anomaly Detection Model

**Algorithm:** Isolation Forest

**Features (15 total):**
1. Login hour (0-23)
2. Login day of week (0-6)
3. Days since last login
4. Login location (lat/long)
5. Distance from usual location (km)
6. Device fingerprint hash
7. Is new device (boolean)
8. Documents accessed (count)
9. Download count
10. Share link created (count)
11. Failed OTP attempts
12. Session duration (minutes)
13. API calls per minute
14. Unique IPs in session
15. Time since account creation (days)

**Training:**
```python
from sklearn.ensemble import IsolationForest
import numpy as np

# Initialize model
model = IsolationForest(
    contamination=0.1,  # 10% anomaly rate
    random_state=42,
    n_estimators=100
)

# Train on user behavior data
X_train = load_user_behavior_data()
model.fit(X_train)

# Predict anomaly score
def calculate_risk_score(user_activity):
    features = extract_features(user_activity)
    anomaly_score = model.decision_function([features])[0]
    
    # Convert to 0-100 scale
    risk_score = int((1 - anomaly_score) * 50 + 50)
    risk_score = max(0, min(100, risk_score))
    
    return risk_score
```

### OCR Implementation

**Using PaddleOCR:**
```python
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

def extract_document_data(image_path):
    # Perform OCR
    result = ocr.ocr(image_path, cls=True)
    
    # Extract text
    text_blocks = []
    for line in result:
        for word_info in line:
            text_blocks.append(word_info[1][0])
    
    # Classify document type
    doc_type = classify_document(text_blocks)
    
    # Extract structured data
    extracted_data = parse_document(doc_type, text_blocks)
    
    return {
        'document_type': doc_type,
        'extracted_data': extracted_data,
        'confidence': calculate_confidence(result)
    }
```

---

## Security Architecture

### Authentication Flow

```
1. User enters email/password
2. Backend validates credentials
3. Generate JWT token (24h expiry)
4. Send OTP to registered phone/email
5. User enters OTP
6. Validate OTP (5 min expiry)
7. Create session
8. Return access token + refresh token
```

### Document Encryption

**At Rest:**
- Algorithm: AES-256-GCM
- Key management: Supabase Vault
- Per-document encryption keys
- Master key rotation: 90 days

**In Transit:**
- TLS 1.3
- Certificate pinning
- HSTS enabled

**Encryption Process:**
```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os

def encrypt_document(file_data, user_id):
    # Generate unique key for this document
    key = os.urandom(32)  # 256-bit key
    iv = os.urandom(12)   # 96-bit IV for GCM
    
    # Encrypt
    cipher = Cipher(
        algorithms.AES(key),
        modes.GCM(iv),
        backend=default_backend()
    )
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(file_data) + encryptor.finalize()
    
    # Store encrypted key (encrypted with master key)
    encrypted_key = encrypt_with_master_key(key, user_id)
    
    return {
        'ciphertext': ciphertext,
        'iv': iv,
        'tag': encryptor.tag,
        'encrypted_key': encrypted_key
    }
```

### Access Control Matrix

| Role | View Docs | Upload | Share | Delete | View Alerts | Lock Users | Manage Admins | Config AI |
|------|-----------|--------|-------|--------|-------------|------------|---------------|-----------|
| User | Own only | ✓ | Own only | Own only | Own only | ✗ | ✗ | ✗ |
| Admin | All | ✗ | ✗ | ✗ | All | ✓ | ✗ | ✗ |
| Super Admin | All | ✗ | ✗ | ✗ | All | ✓ | ✓ | ✓ |

---

## API Endpoints

### Authentication

```
POST /api/auth/register
POST /api/auth/login
POST /api/auth/logout
POST /api/auth/refresh
POST /api/auth/verify-otp
POST /api/auth/resend-otp
```

### Documents

```
GET    /api/documents
POST   /api/documents/upload
GET    /api/documents/:id
DELETE /api/documents/:id
PATCH  /api/documents/:id
GET    /api/documents/:id/download
```

### Sharing

```
POST   /api/shares
GET    /api/shares/:id
DELETE /api/shares/:id
GET    /api/shares/:id/access
POST   /api/shares/:id/verify-otp
```

### Security

```
GET  /api/security/alerts
GET  /api/security/risk-score
POST /api/security/lock-user
POST /api/security/unlock-user
POST /api/security/trigger-voice-call
GET  /api/security/access-logs
```

### Admin

```
GET    /api/admin/users
GET    /api/admin/users/:id
PATCH  /api/admin/users/:id
DELETE /api/admin/users/:id
GET    /api/admin/analytics
POST   /api/admin/admins
DELETE /api/admin/admins/:id
```

### Super Admin

```
GET   /api/superadmin/platform-stats
PATCH /api/superadmin/ai-config
GET   /api/superadmin/system-health
PATCH /api/superadmin/security-policy
```

---

## Database Schema

### Users Table
```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    phone VARCHAR(20),
    role VARCHAR(20) DEFAULT 'user',
    privacy_score INTEGER DEFAULT 50,
    is_locked BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### Documents Table
```sql
CREATE TABLE documents (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    document_type VARCHAR(50) NOT NULL,
    file_path VARCHAR(500) NOT NULL,
    file_size INTEGER,
    blockchain_hash VARCHAR(64),
    blockchain_tx_id VARCHAR(100),
    extracted_data JSONB,
    is_verified BOOLEAN DEFAULT false,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);
```

### Shares Table
```sql
CREATE TABLE shares (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    document_id UUID REFERENCES documents(id) ON DELETE CASCADE,
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    share_token VARCHAR(100) UNIQUE NOT NULL,
    access_limit INTEGER DEFAULT 1,
    access_count INTEGER DEFAULT 0,
    expires_at TIMESTAMP NOT NULL,
    require_otp BOOLEAN DEFAULT true,
    allow_download BOOLEAN DEFAULT false,
    auto_mask BOOLEAN DEFAULT true,
    self_destruct BOOLEAN DEFAULT false,
    is_active BOOLEAN DEFAULT true,
    created_at TIMESTAMP DEFAULT NOW()
);
```

### Security_Alerts Table
```sql
CREATE TABLE security_alerts (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    alert_type VARCHAR(50) NOT NULL,
    risk_score INTEGER NOT NULL,
    event_data JSONB,
    is_resolved BOOLEAN DEFAULT false,
    resolved_by UUID REFERENCES users(id),
    created_at TIMESTAMP DEFAULT NOW(),
    resolved_at TIMESTAMP
);
```

### Access_Logs Table
```sql
CREATE TABLE access_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE CASCADE,
    document_id UUID REFERENCES documents(id) ON DELETE CASCADE,
    action VARCHAR(50) NOT NULL,
    ip_address VARCHAR(45),
    device_info JSONB,
    location JSONB,
    risk_level VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);
```

---

## Deployment Guide

### Frontend (Vercel)

1. **Connect Repository**
   ```bash
   vercel login
   vercel link
   ```

2. **Configure Environment**
   ```
   NEXT_PUBLIC_API_URL=https://api.datavaultsecure.in
   NEXT_PUBLIC_SUPABASE_URL=your_url
   NEXT_PUBLIC_SUPABASE_ANON_KEY=your_key
   ```

3. **Deploy**
   ```bash
   vercel --prod
   ```

### Backend (Render)

1. **Create Web Service**
   - Runtime: Python 3.11
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

2. **Environment Variables**
   ```
   DATABASE_URL=postgresql://...
   SUPABASE_URL=...
   SUPABASE_KEY=...
   JWT_SECRET=...
   TWILIO_SID=...
   TWILIO_TOKEN=...
   ```

3. **Deploy**
   - Push to GitHub
   - Render auto-deploys on push

### Database (Supabase)

1. **Create Project**
   - Go to supabase.com
   - Create new project
   - Note connection string

2. **Run Migrations**
   ```bash
   supabase db push
   ```

3. **Enable RLS**
   ```sql
   ALTER TABLE documents ENABLE ROW LEVEL SECURITY;
   
   CREATE POLICY "Users can view own documents"
   ON documents FOR SELECT
   USING (auth.uid() = user_id);
   ```

---

**End of Documentation**

For questions or contributions, please refer to the main README.md file.
