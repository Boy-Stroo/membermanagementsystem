import datetime
import random
import sqlite3

from Controller.MemberController import MemberController
from MenuMaker import MenuMaker
from Service.MemberService import MemberService
from Service.UserService import UserService
import seeder
from Controller.Controllers import Controllers

from Model.User import User, Role
from Model.MenuItem import MenuItem


# Testing area

memberservice = MemberService()
userservice = UserService()

members = memberservice.get_all()
users = userservice.get_all()

for member in members:
    print(member)

for user in users:
    myuser = User(*user)
    if myuser.role < Role.CONSULTANT:
        print(myuser)


# Uncomment this to run the program
login_page = MenuMaker.define_menu_structure()
while True:
    login_page.execute()