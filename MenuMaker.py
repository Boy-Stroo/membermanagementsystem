from Controller.LoginController import LoginController
from Model.MenuItem import MenuItem
from Model.MenuPage import MenuPage


class MenuMaker:
        
    
    def define_menu_structure():
        login_page = MenuPage("Login")
        home_page = MenuPage("Home")
        member_page = MenuPage("Member")
        user_page = MenuPage("User")
        system_info_page = MenuPage("System Information")

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