import datetime
import random
import sqlite3
# import seeder

from Controller.DataEncrypter import DataEncrypter
from Controller.MemberController import MemberController
from MenuMaker import MenuMaker
from Service.MemberService import MemberService
from Service.UserService import UserService

from Model.User import User, Role
from Model.MenuItem import MenuItem


# Testing area
# seeder.drop()

memberservice = MemberService()
userservice = UserService()
memberservice.create_table()
userservice.create_table()
# seeder.seed()


# for member in members:
#     print(member)

# for user in users:
#     myuser = User(*user)
#     if myuser.role < Role.CONSULTANT:
#         print(myuser)

# Uncomment this to run the program
login_page = MenuMaker.define_menu_structure()
while True:
    login_page.execute()
