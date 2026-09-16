import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-key-change-in-production")

    # When set, the app renders in "static export" mode for platforms with no
    # backend (e.g. Netlify): auth pages are hidden and the quote form uses
    # Netlify Forms instead of posting to Flask/MySQL. See freeze.py.
    STATIC_BUILD = os.environ.get("STATIC_BUILD", "0") == "1"

    # MySQL connection for the `enquiries` table (see database/schema.sql
    # and db.py). Defaults match a local XAMPP/MySQL install (root, no
    # password). Override via environment variables for other setups.
    MYSQL_HOST = os.environ.get("MYSQL_HOST", "localhost")
    MYSQL_PORT = os.environ.get("MYSQL_PORT", "3306")
    MYSQL_USER = os.environ.get("MYSQL_USER", "root")
    MYSQL_PASSWORD = os.environ.get("MYSQL_PASSWORD", "")
    MYSQL_DB = os.environ.get("MYSQL_DB", "gio_electronics")

    UPLOAD_FOLDER = os.path.join(BASE_DIR, "static", "uploads")
    ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg", "dwg", "dxf", "zip"}
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB
