import sqlite3
import hashlib
# ==========================================
# DATABASE CONNECTION
# ==========================================

def connect_db():

    conn = sqlite3.connect(
        "database/finance.db",
        check_same_thread=False
    )

    return conn

# ==========================================
# CREATE TABLES
# ==========================================

def create_tables():

    conn = connect_db()

    cursor = conn.cursor()

    # USERS TABLE

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,
        email TEXT UNIQUE,
        password TEXT
    )
    """)

    # FINANCE RECORDS TABLE

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS finance_records (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        income REAL,
        rent REAL,
        food REAL,
        travel REAL,
        entertainment REAL,
        other_expense REAL,

        total_expense REAL,
        savings REAL,
        savings_rate REAL
    )
    """)

    conn.commit()

    conn.close()

# ==========================================
# SAVE FINANCIAL DATA
# ==========================================

def save_financial_data(
    income,
    rent,
    food,
    travel,
    entertainment,
    other,
    total_expense,
    savings,
    savings_rate
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO finance_records (

        income,
        rent,
        food,
        travel,
        entertainment,
        other_expense,
        total_expense,
        savings,
        savings_rate

    )

    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)

    """, (

        income,
        rent,
        food,
        travel,
        entertainment,
        other,
        total_expense,
        savings,
        savings_rate

    ))

    conn.commit()

    conn.close()

# ==========================================
# FETCH ALL RECORDS
# ==========================================

def fetch_records():

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM finance_records
    """)

    data = cursor.fetchall()

    conn.close()

    return data

# ==========================================
# CREATE USER
# ==========================================

def create_user(
    name,
    email,
    password
):

    conn = connect_db()

    cursor = conn.cursor()

    hashed_password = hashlib.sha256(
        password.encode()
    ).hexdigest()

    try:

        cursor.execute("""
        INSERT INTO users (
            name,
            email,
            password
        )

        VALUES (?, ?, ?)
        """, (
            name,
            email,
            hashed_password
        ))

        conn.commit()

        return True

    except:

        return False

    finally:

        conn.close()

# ==========================================
# LOGIN USER
# ==========================================

def login_user(
    email,
    password
):

    conn = connect_db()

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM users
    WHERE email = ?
    """, (email,))

    user = cursor.fetchone()

    conn.close()

    if user:

        stored_password = user[3]

        hashed_input_password = hashlib.sha256(
            password.encode()
        ).hexdigest()

        if hashed_input_password == stored_password:

            return user

    return None
