import sqlite3

from Controller.DataEncrypter import DataEncrypter
from Controller.MemberController import MemberController
from Controller.InputValidator import InputValidator
from Controller.LogController import LogController
from Controller.UserController import UserController
from Model.Member import Member
from Model.User import User
from Service.MemberService import MemberService
from Service.LogService import LogService
from Service.UserService import UserService

input_validator = InputValidator()
user_service = UserService()
member_service = MemberService()
log_service = LogService()

user_service.create_table()
member_service.create_table()
log_service.create_table()

log_controller = LogController(log_service, input_validator)
user_controller = UserController(user_service, input_validator, log_controller)
member_controller = MemberController(member_service, input_validator, log_controller, user_controller)


members = [
    (member_controller.generate_member_id(), 'John', 'Doe', "25", 'Male', "70", 'Karbonkelstraat 69, 1234AB Rotterdam', 'john@doe.nl', '+31612345678', '2021-01-01'),
    (member_controller.generate_member_id(), 'Jane', 'Doe', "25", 'Female', "60", 'Stationstraat 12, 1234AB Eindhoven', 'jane@doe.nl', '+31612345123', '2021-01-07'),
    (member_controller.generate_member_id(), 'John', 'Smith', "30", 'Other', "80", 'Molenstraat 14, 5321AB Groningen', 'john@smith.nl', '+31656785678', '2021-02-01'),
    (member_controller.generate_member_id(), 'Jane', 'Smith', "30", 'Female', "70", 'Watermolen 32, 1234AB Breda', 'jane@smith.nl', '+31656785123', '2021-02-07')
]

salt = [
    DataEncrypter().generate_salt(),
    DataEncrypter().generate_salt(),
    DataEncrypter().generate_salt(),
    DataEncrypter().generate_salt()
]

users = [
    ("1", 'super_admin', DataEncrypter().hashPassword('Admin_123?', salt[0]), "Super admin", 'John', 'Doe', '2021-01-01', salt[0]),
    ("2", 'admin', DataEncrypter().hashPassword('admin', salt[1]), "System admin", 'Jane', 'Doe', '2021-01-07', salt[1]),
    ("3", 'consultant', DataEncrypter().hashPassword('consultant', salt[2]), "Consultant", 'John', 'Smith', '2021-02-01',salt[2]),
    ("4", 'consultant', DataEncrypter().hashPassword('consultant', salt[3]), "Consultant", 'Jane', 'Smith', '2021-02-07', salt[3])
]

def seed():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    for member in members:
        encrypted_member = DataEncrypter().encrypt_data_list(member)
        c.execute('INSERT INTO members VALUES (?,?,?,?,?,?,?,?,?,?)', encrypted_member)

    for user in users:
        encrypted_user = DataEncrypter().encrypt_data_list(user)
        c.execute('INSERT INTO users VALUES (?,?,?,?,?,?,?,?)', encrypted_user)

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