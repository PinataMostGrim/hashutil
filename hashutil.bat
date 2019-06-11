@echo off
:: Run the hashutil module using its virtual environment.

setlocal
:: In order to support executing this batch from from any location,
:: hashutil's folder must be added to the Python path.
set PYTHONPATH=%~dp0
"%~dp0.venv\Scripts\python.exe" -m hashutil %*
endlocal
