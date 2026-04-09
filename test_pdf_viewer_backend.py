#!/usr/bin/env python3
"""
Test script to verify PDF viewer backend functionality
"""
import requests
import json

BASE_URL = "http://localhost:8001"

def test_login():
    """Test login and get token"""
    print("=" * 60)
    print("TEST 1: Login")
    print("=" * 60)
    
    response = requests.post(
        f"{BASE_URL}/api/auth/login",
        json={
            "email": "user@example.com",
            "password": "password"
        }
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        print(f"✅ Login successful!")
        print(f"Token: {data['access_token'][:50]}...")
        print(f"User: {data['user']['full_name']}")
        return data['access_token']
    else:
        print(f"❌ Login failed: {response.text}")
        return None

def test_get_documents(token):
    """Test getting documents list"""
    print("\n" + "=" * 60)
    print("TEST 2: Get Documents")
    print("=" * 60)
    
    response = requests.get(
        f"{BASE_URL}/api/documents/",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        data = response.json()
        documents = data.get('documents', [])
        print(f"✅ Documents loaded: {len(documents)} documents")
        if documents:
            print(f"First document: {documents[0]['filename']}")
            print(f"Document ID: {documents[0]['id']}")
            return documents[0]['id']
        else:
            print("⚠️  No documents found. Upload one first!")
            return None
    else:
        print(f"❌ Failed to get documents: {response.text}")
        return None

def test_get_document(token, doc_id):
    """Test getting specific document"""
    print("\n" + "=" * 60)
    print("TEST 3: Get Document Details")
    print("=" * 60)
    
    response = requests.get(
        f"{BASE_URL}/api/documents/{doc_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        doc = response.json()
        print(f"✅ Document loaded!")
        print(f"Filename: {doc['filename']}")
        print(f"Content Type: {doc['content_type']}")
        print(f"File Path: {doc['file_path']}")
        print(f"Size: {doc['file_size']} bytes")
        return True
    else:
        print(f"❌ Failed to get document: {response.text}")
        return False

def test_get_file(token, doc_id):
    """Test getting document file"""
    print("\n" + "=" * 60)
    print("TEST 4: Get Document File")
    print("=" * 60)
    
    response = requests.get(
        f"{BASE_URL}/api/documents/{doc_id}/file",
        headers={"Authorization": f"Bearer {token}"}
    )
    
    print(f"Status: {response.status_code}")
    print(f"Headers: {dict(response.headers)}")
    
    if response.status_code == 200:
        print(f"✅ File fetched successfully!")
        print(f"Content Type: {response.headers.get('content-type')}")
        print(f"Content Length: {len(response.content)} bytes")
        return True
    else:
        print(f"❌ Failed to fetch file: {response.text}")
        return False

def test_without_auth(doc_id):
    """Test accessing file without authentication"""
    print("\n" + "=" * 60)
    print("TEST 5: Access Without Authentication (Should Fail)")
    print("=" * 60)
    
    response = requests.get(
        f"{BASE_URL}/api/documents/{doc_id}/file"
    )
    
    print(f"Status: {response.status_code}")
    if response.status_code == 401:
        print(f"✅ Correctly rejected unauthenticated request!")
        return True
    else:
        print(f"⚠️  Expected 401, got {response.status_code}")
        return False

def main():
    print("\n🔧 PDF Viewer Backend Test Suite")
    print("Testing authentication and file serving\n")
    
    # Test 1: Login
    token = test_login()
    if not token:
        print("\n❌ Cannot continue without token")
        return
    
    # Test 2: Get documents
    doc_id = test_get_documents(token)
    if not doc_id:
        print("\n⚠️  No documents to test with. Upload a document first!")
        return
    
    # Test 3: Get document details
    test_get_document(token, doc_id)
    
    # Test 4: Get file with authentication
    test_get_file(token, doc_id)
    
    # Test 5: Try without authentication
    test_without_auth(doc_id)
    
    print("\n" + "=" * 60)
    print("✅ All tests completed!")
    print("=" * 60)
    print("\nIf all tests passed, the backend is working correctly.")
    print("Now test the frontend by:")
    print("1. Open http://localhost:3000/frontend/dashboard.html")
    print("2. Login with user@example.com / password")
    print("3. Click 'View' on a document")
    print("4. Check browser console for detailed logs")

if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.ConnectionError:
        print("\n❌ Cannot connect to backend server!")
        print("Make sure the backend is running on http://localhost:8001")
        print("Run: python backend/app_postgres.py")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
