#!/usr/bin/env python3
"""
Quick API test
"""
import requests
import json

def test_api():
    try:
        print("🧪 Testing Backend API...")
        
        # Test health endpoint
        response = requests.get("http://localhost:8001/health")
        print(f"Health check: {response.status_code}")
        if response.status_code == 200:
            print(f"Response: {response.json()}")
        
        # Test login
        print("\n🔐 Testing Login...")
        login_data = {
            "email": "admin@datavaultsecure.in",
            "password": "password"
        }
        
        response = requests.post("http://localhost:8001/api/auth/login", json=login_data)
        print(f"Login status: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Login successful!")
            print(f"User: {data['user']['full_name']} ({data['user']['role']})")
            print(f"Token: {data['access_token'][:50]}...")
        else:
            print(f"❌ Login failed: {response.text}")
            
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    test_api()