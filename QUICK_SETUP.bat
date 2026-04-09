@echo off
echo ============================================================
echo DataVault Secure - Quick Setup Script
echo ============================================================
echo.

echo Step 1: Setting up clean PostgreSQL database...
cd backend
python setup_clean_database.py
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: Database setup failed!
    echo Please check the error messages above.
    pause
    exit /b 1
)

echo.
echo ============================================================
echo Step 2: Starting backend server...
echo ============================================================
echo.
echo Backend will start on http://localhost:8001
echo Press Ctrl+C to stop the server
echo.
echo After server starts, open frontend/login_professional.html in your browser
echo.
pause

python app_postgres.py
