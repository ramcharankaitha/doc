#!/usr/bin/env python3
"""
Quick test script to verify backend login functionality
"""
import requests
import json

def test_backend():
    print("Testing DataVault Backend...")
    
    # Test 1: Health check
    print("\n1. Testing health endpoint...")
    try:
        response = requests.get("http://localhost:8001/health")
        print(f"Status: {response.status_code}")
        print(f"Response: {response.json()}")
    except Exception as e:
        print(f"Health check failed: {e}")
        return False
    
    # Test 2: Login
    print("\n2. Testing login endpoint...")
    try:
        response = requests.post(
            "http://localhost:8001/api/auth/login",
            json={
                "email": "user@example.com",
                "password": "password"
            },
            headers={"Content-Type": "application/json"}
        )
        print(f"Status: {response.status_code}")
        if response.status_code == 200:
            data = response.json()
            print(f"✅ Login successful!")
            print(f"User: {data['user']['full_name']}")
            print(f"Token: {data['access_token'][:50]}...")
            return True
        else:
            print(f"❌ Login failed: {response.text}")
            return False
    except Exception as e:
        print(f"Login test failed: {e}")
        return False

if __name__ == "__main__":
    test_backend()