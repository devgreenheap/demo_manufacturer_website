"""MySQL access for customer accounts and enquiry (Request a Quote) submissions.

Products remain defined in data.py — this module persists the `customers`
and `enquiries` tables described in database/schema.sql.
"""

import pymysql
from pymysql.err import IntegrityError
from config import Config


def get_connection():
    return pymysql.connect(
        host=Config.MYSQL_HOST,
        port=int(Config.MYSQL_PORT),
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD,
        database=Config.MYSQL_DB,
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor,
        autocommit=True,
    )


def save_enquiry(record):
    record.setdefault("customer_id", None)
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                INSERT INTO enquiries
                    (customer_id, name, company_name, email, phone, product_service, quantity, message, attachment)
                VALUES
                    (%(customer_id)s, %(name)s, %(company_name)s, %(email)s, %(phone)s, %(product_service)s, %(quantity)s, %(message)s, %(attachment)s)
                """,
                record,
            )
    finally:
        conn.close()


def list_enquiries():
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM enquiries ORDER BY created_at DESC")
            return cursor.fetchall()
    finally:
        conn.close()


def list_enquiries_for_customer(customer_id):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT * FROM enquiries WHERE customer_id = %s ORDER BY created_at DESC",
                (customer_id,),
            )
            return cursor.fetchall()
    finally:
        conn.close()


def create_customer(record):
    """Insert a new customer. Returns the new id, or None if the email is
    already registered."""
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            try:
                cursor.execute(
                    """
                    INSERT INTO customers (full_name, company_name, email, phone, password_hash)
                    VALUES (%(full_name)s, %(company_name)s, %(email)s, %(phone)s, %(password_hash)s)
                    """,
                    record,
                )
            except IntegrityError:
                return None
            return cursor.lastrowid
    finally:
        conn.close()


def get_customer_by_email(email):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM customers WHERE email = %s", (email,))
            return cursor.fetchone()
    finally:
        conn.close()


def get_customer_by_id(customer_id):
    conn = get_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM customers WHERE id = %s", (customer_id,))
            return cursor.fetchone()
    finally:
        conn.close()
