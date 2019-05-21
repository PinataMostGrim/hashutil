@echo off
REM: Run checksum.py using the virtual environment '.venv'
%~dp0.venv\Scripts\python.exe %~dp0hashutil.py %*
