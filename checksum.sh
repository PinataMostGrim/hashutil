#!/bin/bash
# Run checksum.py using a virtual environment.

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Note: The windows virtual environment path must still defined in POSIX format.
VENV_WIN_PATH="$SCRIPT_DIR/.venv/Scripts/python.exe"
VENV_LINUX_PATH="$SCRIPT_DIR/.venv/bin/python"

cd "$SCRIPT_DIR"

if [ -e "$VENV_WIN_PATH" ]; then
    "$VENV_WIN_PATH" "checksum.py" "$@"

elif [ -e "$VENV_LINUX_PATH" ]; then
    "$VENV_LINUX_PATH" "checksum.py" "$@"
else
    echo "Virtual environment not found"
fi
