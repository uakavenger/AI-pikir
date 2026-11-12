@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  echo Run setup.bat once before starting the app.
  pause
  exit /b 1
)

".venv\Scripts\python.exe" -m streamlit run app.py --server.address 127.0.0.1
