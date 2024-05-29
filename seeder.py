import sqlite3

def create_tables():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT, role INTEGER)')
    c.execute('CREATE TABLE IF NOT EXISTS members (id TEXT PRIMARY KEY, name TEXT, birthdate TEXT, address TEXT, phone TEXT, email TEXT)')
    conn.commit()
    c.close()

def seed():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('INSERT INTO users (username, password, role) VALUES ("superadmin", "superadmin", 1)')
    c.execute('INSERT INTO users (username, password, role) VALUES ("admin", "admin", 2)')
    c.execute('INSERT INTO users (username, password, role) VALUES ("consultant", "consultant", 3)')
    c.execute('INSERT INTO members (id, name, birthdate, address, phone, email) VALUES ("1", "John Doe", "1990-01-01", "123 Main St, Springfield, IL 62701", "555-555-5555", "dads@dasaaw.fsa")')

    conn.commit()
    c.close()

def clear():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM users')
    c.execute('DELETE FROM members')
    conn.commit()
    c.close()