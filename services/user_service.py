import re, bcrypt
from models.user_model import (
    fetch_all_users, fetch_user_by_id, insert_user,
    update_user, delete_user, find_users_by_name,
    authenticate_user
)

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")

def list_users():
    return fetch_all_users()

def get_user(uid):
    user = fetch_user_by_id(uid)
    if not user:
        raise ValueError("User not found")
    return user

def create_user(data):
    name  = data.get("name","").strip()
    email = data.get("email","").strip()
    pw    = data.get("password","")
    if not name or not EMAIL_REGEX.fullmatch(email) or len(pw) < 6:
        raise ValueError("Invalid input")
    pw_hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
    new_id = insert_user(name, email, pw_hash)
    return get_user(new_id)

def modify_user(uid, data):
    name  = data.get("name","").strip()
    email = data.get("email","").strip()
    if not name or not EMAIL_REGEX.fullmatch(email):
        raise ValueError("Invalid input")
    update_user(uid, name, email)
    return get_user(uid)

def remove_user(uid):
    if not fetch_user_by_id(uid):
        raise ValueError("User not found")
    delete_user(uid)

def search_by_name(name):
    if not name.strip():
        raise ValueError("Name query is empty")
    return find_users_by_name(name)

def login_user(data):
    email = data.get("email","").strip()
    pw    = data.get("password","")
    uid   = authenticate_user(email, pw)
    if not uid:
        raise ValueError("Invalid credentials")
    return uid
