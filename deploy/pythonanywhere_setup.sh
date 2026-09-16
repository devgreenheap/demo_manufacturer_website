#!/bin/bash
# GIO Electronics — one-shot PythonAnywhere setup.
#
# Run this FROM A BASH CONSOLE ON PYTHONANYWHERE (not on your own machine).
#
# Before running:
#   1. Upload GioElectronics_deploy.zip via the Files tab into your home dir.
#   2. Set your MySQL password on the Databases tab.
#   3. On the Web tab, click "Add a new web app" -> Manual configuration
#      (any Python version placeholder is fine — this script overwrites it).
#
# Then run:  bash pythonanywhere_setup.sh

set -e

echo "=== GIO Electronics setup ==="
echo

read -p "Your PythonAnywhere username: " PA_USER
read -sp "MySQL password (set on the Databases tab): " MYSQL_PW
echo
read -p "Python version for the web app (e.g. 3.10): " PY_VERSION

SECRET=$(python3 -c "import secrets; print(secrets.token_hex(32))")

HOME_DIR="/home/$PA_USER"
ZIP_PATH="$HOME_DIR/GioElectronics_deploy.zip"
PROJECT_DIR="$HOME_DIR/gio_electronics"
WSGI_PATH="/var/www/${PA_USER}_pythonanywhere_com_wsgi.py"
VENV_NAME="gio-venv"

if [ ! -f "$ZIP_PATH" ]; then
  echo "ERROR: $ZIP_PATH not found."
  echo "Upload GioElectronics_deploy.zip via the Files tab first, then re-run this script."
  exit 1
fi

if [ ! -f "$WSGI_PATH" ]; then
  echo "ERROR: $WSGI_PATH not found."
  echo "Go to the Web tab and click 'Add a new web app' first (Manual configuration), then re-run this script."
  exit 1
fi

echo "Unpacking project..."
unzip -o "$ZIP_PATH" -d "$PROJECT_DIR" > /dev/null
cd "$PROJECT_DIR"

if [ -d "$HOME_DIR/.virtualenvs/$VENV_NAME" ]; then
  echo "Virtualenv already exists, reusing it."
  workon "$VENV_NAME"
else
  echo "Creating virtualenv..."
  mkvirtualenv --python="/usr/bin/python$PY_VERSION" "$VENV_NAME"
fi

echo "Installing dependencies..."
pip install -q -r requirements.txt

echo "Writing WSGI configuration..."
cat > "$WSGI_PATH" <<EOF
import sys, os

path = '$PROJECT_DIR'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['SECRET_KEY'] = '$SECRET'
os.environ['MYSQL_HOST'] = '${PA_USER}.mysql.pythonanywhere-services.com'
os.environ['MYSQL_USER'] = '$PA_USER'
os.environ['MYSQL_PASSWORD'] = '$MYSQL_PW'
os.environ['MYSQL_DB'] = '${PA_USER}\$default'

from app import app as application
EOF

echo
echo "=== Done ==="
echo "Project directory : $PROJECT_DIR"
echo "Virtualenv         : $VENV_NAME"
echo "WSGI file written  : $WSGI_PATH"
echo
echo "Remaining manual steps on the Web tab:"
echo "  1. Set 'Virtualenv' to: $HOME_DIR/.virtualenvs/$VENV_NAME"
echo "  2. Set 'Source code' / working directory to: $PROJECT_DIR"
echo "  3. Make sure the database tables exist yet? Run deploy/schema_pythonanywhere.sql"
echo "     via the 'Execute SQL statement' box on the Databases tab if you haven't."
echo "  4. Click the big green Reload button."
echo "  5. Visit https://${PA_USER}.pythonanywhere.com"
