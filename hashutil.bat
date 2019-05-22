@echo off
REM: Run hashutil_cli.py using the virtual environment '.venv'
%~dp0.venv\Scripts\python.exe %~dp0hashutil_cli.py %*
