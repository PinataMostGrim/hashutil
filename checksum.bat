@echo off
REM: Run checksum.py using virtual environment '.\venv'
%~dp0.venv\Scripts\python.exe %~dp0checksum.py %*
