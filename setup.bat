@echo off
setlocal
cd /d "%~dp0"

echo [1/3] Creating the Python virtual environment...
if not exist ".venv\Scripts\python.exe" py -3.11 -m venv .venv
if errorlevel 1 goto failed

echo [2/3] Installing the required packages...
".venv\Scripts\python.exe" -m pip install -r requirements.txt
if errorlevel 1 goto failed

echo [3/3] Training the model and writing evaluation results...
".venv\Scripts\python.exe" src\train_model.py
if errorlevel 1 goto failed

echo.
echo Setup is complete. Double-click run_app.bat to start the app.
pause
exit /b 0

:failed
echo.
echo Setup stopped because a step failed. Check the message above and README.md.
pause
exit /b 1
