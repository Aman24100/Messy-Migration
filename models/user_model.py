import sqlite3
from flask import current_app

def get_db():
    db = sqlite3.connect(current_app.config["DATABASE"])
    db.row_factory = sqlite3.Row
    return db

def fetch_all_users():
    cur = get_db().execute("SELECT id, name, email FROM users")
    return [dict(r) for r in cur.fetchall()]

def fetch_user_by_id(uid):
    cur = get_db().execute("SELECT id, name, email FROM users WHERE id = ?", (uid,))
    row = cur.fetchone()
    return dict(row) if row else None

def insert_user(name, email, pw_hash):
    db = get_db()
    cur = db.execute(
        "INSERT INTO users (name, email, password) VALUES (?, ?, ?)",
        (name, email, pw_hash)
    )
    db.commit()
    return cur.lastrowid

def update_user(uid, name, email):
    db = get_db()
    db.execute(
        "UPDATE users SET name = ?, email = ? WHERE id = ?",
        (name, email, uid)
    )
    db.commit()

def delete_user(uid):
    db = get_db()
    db.execute("DELETE FROM users WHERE id = ?", (uid,))
    db.commit()

def find_users_by_name(name):
    pattern = f"%{name}%"
    cur = get_db().execute(
        "SELECT id, name, email FROM users WHERE name LIKE ?",
        (pattern,)
    )
    return [dict(r) for r in cur.fetchall()]

def authenticate_user(email, password):
    import bcrypt
    cur = get_db().execute(
        "SELECT id, password FROM users WHERE email = ?",
        (email,)
    )
    row = cur.fetchone()
    if row and bcrypt.checkpw(password.encode(), row["password"]):
        return row["id"]
    return None
