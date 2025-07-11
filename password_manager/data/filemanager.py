import os
import sqlite3

DATA_DIR = os.path.dirname(__file__)
HASH_PATH = os.path.join(DATA_DIR, "password.hash")
VAULT_PATH = os.path.join(DATA_DIR, "vault.db")
def save_hash(hashed_password):
    file = open(HASH_PATH, "w")
    file.write(hashed_password)
    file.close()

def get_hash():
    file = open(HASH_PATH, "r")
    hashed_password = file.read()
    file.close()
    return hashed_password
    
def hash_exists():
    return os.path.exists(HASH_PATH)

def create_vault():
    conn = sqlite3.connect(VAULT_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS passwords (
            name TEXT NOT NULL PRIMARY KEY,
            email TEXT,
            username TEXT,
            password TEXT NOT NULL,
            url TEXT,
            notes TEXT
        )
    ''')
    conn.commit()
    conn.close()
def add_password_to_vault(name, email, username, password, url, notes):
    conn = sqlite3.connect(VAULT_PATH)
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO passwords (name, email, username, password, url, notes)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (name, email, username, password, url, notes))
    conn.commit()
    conn.close()
def print_db():
    conn = sqlite3.connect(VAULT_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM passwords')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()
def get_passwords_by_name(search_term):
    conn = sqlite3.connect(VAULT_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM passwords WHERE name LIKE ?', (f'%{search_term}%',))
    rows = cursor.fetchall()
    conn.close()
    return rows
def get_password_by_name(name):
    conn = sqlite3.connect(VAULT_PATH)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM passwords WHERE name = ?', (name,))
    row = cursor.fetchone()
    conn.close()
    return row if row else None