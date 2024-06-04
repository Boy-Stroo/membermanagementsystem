from Controller.LoginController import LoginController
from Controller.UIFormatter import UIFormatter
from Model.CollectionMenuPage import CollectionMenuPage
from Model.MenuItem import MenuItem
from Model.MenuPage import MenuPage
from Service.Service import Service
from Service.UserService import UserService


class MenuMaker:
        
    
    def define_menu_structure():
        formatter = UIFormatter()
        user_service = UserService()


        login_page = MenuPage("Login", formatter)
        home_page = MenuPage("Home", formatter)
        member_page = MenuPage("Member", formatter)
        user_page = CollectionMenuPage("User", user_service, formatter)
        system_info_page = MenuPage("System Information", formatter)

        login_controller = LoginController()



        login_page.add_menu_item(MenuItem("Login", login_controller.check_login, home_page))
        login_page.add_menu_item(MenuItem("Quit", login_page.quit))


        home_page.add_menu_item(MenuItem("Member", None, member_page))
        home_page.add_menu_item(MenuItem("User", None, user_page))
        home_page.add_menu_item(MenuItem("System Information", None, system_info_page))
        home_page.add_menu_item(MenuItem("Logout", home_page.quit, login_page))

        member_page.add_menu_item(MenuItem("Back", member_page.quit, None))

        user_page.add_menu_item(MenuItem("Back", user_page.quit, None))

        system_info_page.add_menu_item(MenuItem("Back", system_info_page.quit, None))
        
        return login_page