@echo off

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Python is not installed. Please install Python and try again.
    exit /b
)

REM Create a virtual environment named .venv
echo Creating virtual environment...
python -m venv .venv

REM Activate the virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Install the requirements from requirements.txt
echo Installing requirements...
pip install -r requirements.txt

REM Deactivate the virtual environment
echo Deactivating virtual environment...
deactivate

echo Done.
