#!/usr/bin/env python3
"""
DataVault Secure - Master Startup Script
Starts both backend and frontend servers
Usage: python start.py
"""
import subprocess
import sys
import time
import os
from pathlib import Path

def start_backend():
    """Start the backend server"""
    backend_dir = Path("backend")
    if not backend_dir.exists():
        print("❌ Backend directory not found!")
        return None
    
    print("🚀 Starting Backend Server...")
    
    # Check if virtual environment exists
    venv_path = backend_dir / "venv"
    if venv_path.exists():
        # Use virtual environment
        if os.name == 'nt':  # Windows
            python_exe = venv_path / "Scripts" / "python.exe"
        else:  # Linux/Mac
            python_exe = venv_path / "bin" / "python"
    else:
        python_exe = "python"
    
    try:
        backend_process = subprocess.Popen(
            [str(python_exe), "app.py"],
            cwd=backend_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )
        return backend_process
    except Exception as e:
        print(f"❌ Failed to start backend: {e}")
        return None

def start_frontend():
    """Start the frontend server"""
    frontend_dir = Path("frontend")
    if not frontend_dir.exists():
        print("❌ Frontend directory not found!")
        return None
    
    print("🌐 Starting Frontend Server...")
    
    try:
        frontend_process = subprocess.Popen(
            ["python", "app.py"],
            cwd=frontend_dir,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1
        )
        return frontend_process
    except Exception as e:
        print(f"❌ Failed to start frontend: {e}")
        return None

def main():
    print("=" * 70)
    print("🔐 DataVault Secure - Full Stack Startup")
    print("=" * 70)
    print()
    
    # Start backend
    backend_process = start_backend()
    if not backend_process:
        print("❌ Failed to start backend server")
        return
    
    # Wait a moment for backend to start
    time.sleep(2)
    
    # Start frontend
    frontend_process = start_frontend()
    if not frontend_process:
        print("❌ Failed to start frontend server")
        if backend_process:
            backend_process.terminate()
        return
    
    # Wait a moment for both to start
    time.sleep(3)
    
    print("\n" + "=" * 70)
    print("✅ Both servers are starting up!")
    print("=" * 70)
    print()
    print("🔗 Application URLs:")
    print("   🌐 Frontend: http://localhost:3000/index.html")
    print("   🔐 Login: http://localhost:3000/login.html")
    print("   📊 Dashboard: http://localhost:3000/dashboard.html")
    print("   👨‍💼 Admin: http://localhost:3000/admin.html")
    print("   🔧 Super Admin: http://localhost:3000/superadmin.html")
    print()
    print("🔗 Backend URLs:")
    print("   🚀 API: http://localhost:8001")
    print("   📚 API Docs: http://localhost:8001/api/docs")
    print("   🧪 Test: http://localhost:8001/api/test")
    print()
    print("🔐 Test Accounts:")
    print("   Super Admin: admin@datavaultsecure.in / password")
    print("   Admin: admin@example.com / password")
    print("   User: user@example.com / password")
    print()
    print("⏹️  Press Ctrl+C to stop both servers")
    print("=" * 70)
    
    try:
        # Keep the script running and monitor processes
        while True:
            # Check if processes are still running
            if backend_process.poll() is not None:
                print("\n❌ Backend server stopped unexpectedly")
                break
            if frontend_process.poll() is not None:
                print("\n❌ Frontend server stopped unexpectedly")
                break
            
            time.sleep(1)
    
    except KeyboardInterrupt:
        print("\n\n🛑 Shutting down servers...")
        
        # Terminate processes
        if backend_process:
            backend_process.terminate()
            print("✅ Backend server stopped")
        
        if frontend_process:
            frontend_process.terminate()
            print("✅ Frontend server stopped")
        
        print("\n👋 DataVault Secure stopped successfully!")

if __name__ == "__main__":
    main()