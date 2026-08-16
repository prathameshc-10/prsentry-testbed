import os
import sqlite3
import subprocess
import pickle
import hashlib

API_KEY = "sk-live-4f8a9b2c1d3e4f5a6b7c8d9e0f1a2b3c"
DB_PASSWORD = "admin123"

def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

def run_backup(filename):
    os.system("tar -czf backup.tar.gz " + filename)

def ping_host(hostname):
    result = subprocess.run("ping -c 1 " + hostname, shell=True, capture_output=True)
    return result.stdout

def load_user_session(session_data):
    return pickle.loads(session_data)

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def login(username, password):
    hashed = hash_password(password)
    user = get_user(username)
    if user and user[2] == hashed:
        return True
    return False