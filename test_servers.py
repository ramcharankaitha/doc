#!/usr/bin/env python3
"""
Test script to verify both servers are working
"""
import requests
import time

def test_backend():
    """Test backend server"""
    try:
        print("🧪 Testing Backend Server...")
        response = requests.get("http://localhost:8001/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Backend: {data['message']}")
            print(f"   Users: {data['users_count']}")
            return True
        else:
            print(f"❌ Backend returned status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Backend test failed: {e}")
        return False

def test_frontend():
    """Test frontend server"""
    try:
        print("🧪 Testing Frontend Server...")
        response = requests.get("http://localhost:3000/index.html", timeout=5)
        if response.status_code == 200:
            print("✅ Frontend: Serving files successfully")
            return True
        else:
            print(f"❌ Frontend returned status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Frontend test failed: {e}")
        return False

def test_login():
    """Test login functionality"""
    try:
        print("🧪 Testing Login API...")
        login_data = {
            "email": "admin@datavaultsecure.in",
            "password": "password"
        }
        response = requests.post("http://localhost:8001/api/auth/login", json=login_data, timeout=5)
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Login: Successfully authenticated as {data['user']['full_name']}")
            return True
        else:
            print(f"❌ Login failed with status: {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Login test failed: {e}")
        return False

def main():
    print("=" * 60)
    print("🔍 DataVault Secure - Server Test")
    print("=" * 60)
    print()
    
    # Wait a moment for servers to be ready
    print("⏳ Waiting for servers to be ready...")
    time.sleep(3)
    
    backend_ok = test_backend()
    frontend_ok = test_frontend()
    login_ok = test_login()
    
    print()
    print("=" * 60)
    print("📊 Test Results:")
    print(f"   Backend: {'✅ PASS' if backend_ok else '❌ FAIL'}")
    print(f"   Frontend: {'✅ PASS' if frontend_ok else '❌ FAIL'}")
    print(f"   Login: {'✅ PASS' if login_ok else '❌ FAIL'}")
    print("=" * 60)
    
    if backend_ok and frontend_ok and login_ok:
        print("🎉 All tests passed! Your application is ready to use.")
        print()
        print("🌐 Open your browser and go to:")
        print("   http://localhost:3000/login.html")
        print()
        print("🔐 Test with these accounts:")
        print("   admin@datavaultsecure.in / password")
        print("   admin@example.com / password")
        print("   user@example.com / password")
    else:
        print("❌ Some tests failed. Please check the server logs.")

if __name__ == "__main__":
    main()