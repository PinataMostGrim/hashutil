#!/bin/bash
# Run __main__.py using a virtual environment.

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
VENV_ACTIVATE_PATH="$SCRIPT_DIR/.venv/bin/activate"

cd "$SCRIPT_DIR"

source "$VENV_ACTIVATE_PATH"
python -m hashutil "$@"
deactivate
