import sqlite3

from Controller.DataEncrypter import DataEncrypter
from Model.Member import Member
from Model.User import User

members = [
    ("1", 'John Doe', '1990-01-01', '123 Main St, Springfield, IL 62701', '555-555-5555', 'john_doe@gmail.com', '2021-01-01'),
    ("2", 'Jane Doe', '1990-01-01', '123 Main St, Springfield, IL 62701', '555-555-5555', 'jane_doe@gmail.com', '2021-01-07'),
    ("3", 'John Smith', '1990-01-01', '123 Main St, Springfield, IL 62701', '555-555-5555', 'john_smith@yahoo.com', '2021-02-01'),
    ("4", 'Jane Smith', '1990-01-01', '123 Main St, Springfield, IL 62701', '555-555-5555', 'jane_smith@outlook.com', '2021-02-07')
]

users = [
    ("1", 'superadmin', 'superadmin', "1", 'John', 'Doe', '2021-01-01'),
    ("2", 'admin', 'admin', "2", 'Jane', 'Doe', '2021-01-07'),
    ("3", 'consultant', 'consultant', "3", 'John', 'Smith', '2021-02-01'),
    ("4", 'consultant', 'consultant', "3", 'Jane', 'Smith', '2021-02-07')
]

def seed():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    for member in members:
        encrypted_member = DataEncrypter().encrypt_data(member)
        c.execute('INSERT INTO members VALUES (?,?,?,?,?,?,?)', encrypted_member)

    for user in users:
        encrypted_user = DataEncrypter().encrypt_data(user)
        c.execute('INSERT INTO users VALUES (?,?,?,?,?,?,?)', encrypted_user)

    conn.commit()
    c.close()

def clear():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DELETE FROM users')
    c.execute('DELETE FROM members')
    conn.commit()
    c.close()

def drop():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    c.execute('DROP TABLE users')
    c.execute('DROP TABLE members')
    conn.commit()
    c.close()