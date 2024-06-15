import sqlite3

from Controller.DataEncrypter import DataEncrypter
from Controller.MemberController import MemberController
from Controller.InputValidator import InputValidator
from Model.Member import Member
from Model.User import User
from Service.MemberService import MemberService

input_validator = InputValidator()
member_service = MemberService()
member_controller = MemberController(member_service, input_validator)


members = [
    (member_controller.generate_member_id(), 'John', 'Doe', "25", 'Male', "70", 'Karbonkelstraat 69, 1234AB Rotterdam', 'john@doe.nl', '+31612345678', '2021-01-01'),
    (member_controller.generate_member_id(), 'Jane', 'Doe', "25", 'Female', "60", 'Stationstraat 12, 1234AB Eindhoven', 'jane@doe.nl', '+31612345123', '2021-01-07'),
    (member_controller.generate_member_id(), 'John', 'Smith', "30", 'Other', "80", 'Molenstraat 14, 5321AB Groningen', 'john@smith.nl', '+31656785678', '2021-02-01'),
    (member_controller.generate_member_id(), 'Jane', 'Smith', "30", 'Female', "70", 'Watermolen 32, 1234AB Breda', 'jane@smith.nl', '+31656785123', '2021-02-07')
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
        c.execute('INSERT INTO members VALUES (?,?,?,?,?,?,?,?,?,?)', encrypted_member)

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