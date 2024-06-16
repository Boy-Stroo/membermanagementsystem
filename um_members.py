# import seeder

# Boy Stroo (1061579), Jasper Verzijl (1057020), Martin Pietersen (1059195)

from MenuMaker import MenuMaker
from Service.MemberService import MemberService
from Service.UserService import UserService
from Service.LogService import LogService



# Testing area
# seeder.drop()

memberservice = MemberService()
logservice = LogService()
userservice = UserService()
memberservice.create_table()
userservice.create_table()
logservice.create_table()
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
