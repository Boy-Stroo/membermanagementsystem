from Controller.LoginController import LoginController
from Model.MenuItem import MenuItem
from Model.MenuPage import MenuPage


class MenuMaker:
        
    
    def define_menu_structure():
        login_page = MenuPage("Login")
        home_page = MenuPage("Home")

        login_controller = LoginController()

        
        login_page.add_menu_item(MenuItem("Login", login_controller.check_login, home_page))
        login_page.add_menu_item(MenuItem("Quit", login_page.quit))

        home_page.add_menu_item(MenuItem("Logout", home_page.quit, login_page))
        
        return login_page