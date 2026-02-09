import sqlite3
import os

DB_PATH = "/data/app.db"

def get_db():
    os.makedirs("/data", exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db():
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)

    count = cur.execute("SELECT COUNT(*) FROM users").fetchone()[0]

    if count == 0:
        cur.execute("INSERT INTO users VALUES (NULL, 'guest', 'guest123')")
        cur.execute("INSERT INTO users VALUES (NULL, 'admin', 'verysecretpassword')")
        conn.commit()

    conn.close()
