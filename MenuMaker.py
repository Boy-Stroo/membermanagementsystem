from Controller.LoginController import LoginController
from Controller.UIFormatter import UIFormatter
from Model.CollectionMenuPage import CollectionMenuPage
from Model.MenuItem import MenuItem
from Model.MenuPage import MenuPage
from Service.MemberService import MemberService
from Service.Service import Service
from Service.UserService import UserService
from Service.MemberService import MemberService
from Controller.UserController import UserController
from Controller.MemberController import MemberController
from Controller.CollectionController import CollectionController


class MenuMaker:
        
    
    def define_menu_structure():
        formatter = UIFormatter()
        user_service = UserService()
        member_service = MemberService()


        login_page = MenuPage("Login", formatter)
        home_page = MenuPage("Home", formatter)
        member_page = CollectionMenuPage("Member", member_service, formatter)
        user_page = CollectionMenuPage("User", user_service, formatter)
        system_info_page = MenuPage("System Information", formatter)

        login_controller = LoginController()
        user_controller = UserController()
        member_controller = MemberController()
        collection_controller = CollectionController()



        login_page.add_menu_item(MenuItem("Login", login_controller.check_login, home_page))
        login_page.add_menu_item(MenuItem("Quit", login_page.quit))


        home_page.add_menu_item(MenuItem("Member", None, member_page))
        home_page.add_menu_item(MenuItem("User", None, user_page))
        home_page.add_menu_item(MenuItem("System Information", None, system_info_page))
        home_page.add_menu_item(MenuItem("Forgot own password", user_controller.forgot_own_password))
        home_page.add_menu_item(MenuItem("Logout", home_page.quit, login_page))

        member_page.add_menu_item(MenuItem("Add new member", member_controller.add_new_member))
        member_page.add_menu_item(MenuItem("Update member", member_controller.update_member))
        member_page.add_menu_item(MenuItem("Remove member", member_controller.remove_member))
        member_page.add_menu_item(MenuItem("Filter members", collection_controller.filter, arg=member_page))
        member_page.add_menu_item(MenuItem("Back", member_page.quit))

        user_page.add_menu_item(MenuItem("Add new user", user_controller.add_new_user))
        user_page.add_menu_item(MenuItem("Update user", user_controller.update_user))
        user_page.add_menu_item(MenuItem("Remove user", user_controller.remove_user))
        user_page.add_menu_item(MenuItem("Filter users", collection_controller.filter, arg=user_page))
        user_page.add_menu_item(MenuItem("Reset users password (SA)", user_controller.reset_user_password))
        user_page.add_menu_item(MenuItem("Back", user_page.quit))

        system_info_page.add_menu_item(MenuItem("Back", system_info_page.quit))


        
        return login_page
    
if __name__ == "__main__":
    menu = MenuMaker.define_menu_structure()