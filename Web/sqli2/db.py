import sqlite3
import os

DB_PATH = "/data/app.db"

def get_db():
    os.makedirs("/data", exist_ok=True)
    return sqlite3.connect(DB_PATH, check_same_thread=False)

def init_db(flag_value):
    conn = get_db()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS secrets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            secret TEXT
        )
    """)

    # Seed users only once
    if cur.execute("SELECT COUNT(*) FROM users").fetchone()[0] == 0:
        users = [
            "alice",
            "adam",
            "bob",
            "charlie",
            "david",
            "sarah",
            "maria",
            "admin_test"
        ]
        for u in users:
            cur.execute("INSERT INTO users VALUES (NULL, ?)", (u,))

    # Seed flag only once
    if cur.execute("SELECT COUNT(*) FROM secrets").fetchone()[0] == 0:
        cur.execute("INSERT INTO secrets VALUES (NULL, ?)", (flag_value,))

    conn.commit()
    conn.close()
