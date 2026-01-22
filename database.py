
import sqlite3
import random

DB_NAME = "bank.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def create_table():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fullname TEXT,
            mobile TEXT,
            email TEXT,
            account_no TEXT UNIQUE,
            password TEXT,
            pin TEXT,
            balance INTEGER DEFAULT 500
        )
    """)
    conn.commit()
    conn.close()





def create_transactions_table():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_no TEXT,
        txn_type TEXT,
        amount INTEGER,
        balance_after INTEGER,
        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()    




def generate_account_no():
    return str(random.randint(1000000000, 9999999999))




def insert_user(fullname, mobile, email, account_no, password, pin):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO users (fullname, mobile, email, account_no, password, pin, balance)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (fullname, mobile, email, account_no, password, pin, 500))
    conn.commit()
    conn.close()





def get_user_by_name_password(name, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT fullname, mobile, email, account_no, password, pin
        FROM users
        WHERE fullname=? AND password=?
    """, (name, password))
    user = cur.fetchone()
    conn.close()
    return user
    



def get_user_by_account_no(account_no):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE account_no=?", (account_no,))
    user = cur.fetchone()
    conn.close()
    return user




def get_balance(account_no):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT balance FROM users WHERE account_no=?", (account_no,))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else None




def update_balance(account_no, new_balance):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("UPDATE users SET balance=? WHERE account_no=?", (new_balance, account_no))
    conn.commit()
    conn.close()

def insert_transaction(account_no, txn_type, amount, balance_after):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO transactions (account_no, txn_type, amount, balance_after)
    VALUES (?, ?, ?, ?)
    """, (account_no, txn_type, amount, balance_after))

    conn.commit()
    conn.close()


def get_last_transaction(account_no):
    conn = sqlite3.connect("bank.db")
    cursor = conn.cursor()

    cursor.execute("""
    SELECT type, amount, balance_after, timestamp
    FROM transactions
    WHERE account_no = ?
    ORDER BY id DESC
    LIMIT 1
    """, (account_no,))

    data = cursor.fetchone()
    conn.close()
    return data    

def get_last_n_transactions(account_no, limit=5):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(f"""
    SELECT txn_type, amount, balance_after, date
    FROM transactions
    WHERE account_no = ?
    ORDER BY id DESC
    LIMIT {limit}
    """, (account_no,))

    rows = cur.fetchall()
    conn.close()
    return rows


