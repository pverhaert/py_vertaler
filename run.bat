@echo off

REM Check if the virtual environment exists
if not exist .venv (
    echo Virtual environment not found. Please create it first.
    exit /b
)

REM Activate the virtual environment
echo Activating virtual environment...
call .venv\Scripts\activate.bat

REM Start the Streamlit application
echo Starting Streamlit application...
echo Stop the application with Ctrl + c
streamlit run main.py

REM Deactivate the virtual environment after the application is closed
echo Deactivating virtual environment...
deactivate

echo Done.