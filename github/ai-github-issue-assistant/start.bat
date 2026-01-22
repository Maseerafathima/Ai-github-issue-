@echo off
REM Quick Start Script for AI GitHub Issue Assistant

echo.
echo ========================================
echo AI GitHub Issue Assistant - Quick Start
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python from https://www.python.org/
    pause
    exit /b 1
)

echo [1/3] Installing dependencies...
python -m pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo Error: Failed to install dependencies
    pause
    exit /b 1
)

echo [2/3] Checking environment...
if not exist .env (
    copy .env.example .env
    echo Created .env file
)

REM Check if API key is set
for /f "tokens=2 delims==" %%A in ('findstr /R "^OPENAI_API_KEY=" .env') do set "API_KEY=%%A"

if "%API_KEY%"=="" (
    echo.
    echo ===============================================
    echo  SETUP REQUIRED: OpenAI API Key Missing
    echo ===============================================
    echo.
    echo 1. Open: START_HERE.md for step-by-step instructions
    echo 2. Or visit: https://platform.openai.com/api-keys
    echo 3. Get your OpenAI API key (free trial credits available)
    echo 4. Add to .env file: OPENAI_API_KEY=your_key_here
    echo 5. Run this script again
    echo.
    echo ===============================================
    pause
    exit /b 1
)

echo [3/3] Starting Streamlit app...
echo.
echo The app will open in your browser at http://localhost:8501
echo Press Ctrl+C to stop the server
echo.

python -m streamlit run app.py

pause
