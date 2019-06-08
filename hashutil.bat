@echo off
REM: Run hashutil module using the virtual environment '.venv'
"%~dp0.venv\Scripts\activate.bat" && "%~dp0.venv\Scripts\python.exe" -m hashutil %* & "%~dp0.venv\Scripts\deactivate.bat"
