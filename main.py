import datetime
import random
import sqlite3

from Controller.MemberController import MemberController
from MenuMaker import MenuMaker
import seeder

from Model.User import User, Role
from Model.MenuItem import MenuItem


login_page = MenuMaker.define_menu_structure()

while True:
    login_page.execute()