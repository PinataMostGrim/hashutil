@echo off
:: Run __main__.py using the virtual environment '.venv'
"%~dp0.venv\Scripts\python.exe" -m hashutil %*
