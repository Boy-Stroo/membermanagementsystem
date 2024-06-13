import datetime
import random
import sqlite3

from Controller.DataEncrypter import DataEncrypter
from Controller.MemberController import MemberController
from MenuMaker import MenuMaker
from Service.MemberService import MemberService
from Service.UserService import UserService
import seeder
from Controller.Controllers import Controllers

from Model.User import User, Role
from Model.MenuItem import MenuItem



# Testing area
seeder.drop()

memberservice = MemberService()
userservice = UserService()
memberservice.create_table()
userservice.create_table()
seeder.seed()

members = memberservice.get_all()
users = userservice.get_all()

for member in members:
    unencrypted_member = DataEncrypter().decrypt_data(member)
    print(unencrypted_member)


# Uncomment this to run the program
login_page = MenuMaker.define_menu_structure()
while True:
    login_page.execute()
