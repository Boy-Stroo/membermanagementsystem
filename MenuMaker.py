from Controller.LoginController import LoginController
from Controller.UIFormatter import UIFormatter
from Model.CollectionMenuPage import CollectionMenuPage
from Model.MenuItem import MenuItem
from Model.MenuPage import MenuPage
from Service.MemberService import MemberService
from Service.UserService import UserService
from Service.MemberService import MemberService
from Service.LogService import LogService
from Controller.MemberController import MemberController
from Controller.UserController import UserController
from Controller.InputValidator import InputValidator
from Controller.LogController import LogController
from Controller.Logger import Logger



class MenuMaker:

    
    def define_menu_structure():
        input_validator = InputValidator()

        formatter = UIFormatter()
        user_service = UserService()
        member_service = MemberService()
        log_service = LogService()


        log_controller = LogController(log_service, input_validator)
        user_controller = UserController(user_service, input_validator, log_controller)
        member_controller = MemberController(member_service, input_validator, log_controller, user_controller)
        login_controller = LoginController(user_controller, log_controller, input_validator)

        login_page = MenuPage("Login", formatter, user_controller)
        home_page = MenuPage("Home",formatter, user_controller)
        member_page = CollectionMenuPage("Member", member_controller, formatter, user_controller)
        user_page = CollectionMenuPage("User", user_controller,formatter, user_controller)
        system_logs_page = CollectionMenuPage("System Logs", log_controller, formatter, user_controller)



        login_page.add_menu_item(MenuItem("Login", login_controller.check_login, home_page))
        login_page.add_menu_item(MenuItem("Quit", login_page.quit))


        home_page.add_menu_item(MenuItem("Member", None, member_page))
        home_page.add_menu_item(MenuItem("User", None, user_page, level=2))
        home_page.add_menu_item(MenuItem("System Logs", None, system_logs_page, level=2))
        home_page.add_menu_item(MenuItem("Change own password", user_controller.change_own_password, level=2))
        home_page.add_menu_item(MenuItem("Logout", home_page.quit, login_page))

        member_page.add_menu_item(MenuItem("Add new member", member_controller.add_new_member))
        member_page.add_menu_item(MenuItem("Update member", member_controller.update_member))
        member_page.add_menu_item(MenuItem("Remove member", member_controller.remove_member))
        member_page.add_menu_item(MenuItem("Filter members", member_controller.filter))
        member_page.add_menu_item(MenuItem("Reset filter", member_controller.reset_filter))
        member_page.add_menu_item(MenuItem("Back", member_page.quit))

        user_page.add_menu_item(MenuItem("Add new user", user_controller.add_new_user, level=2))
        user_page.add_menu_item(MenuItem("Update user", user_controller.update_user, level=2))
        user_page.add_menu_item(MenuItem("Remove user", user_controller.remove_user, level=2))
        user_page.add_menu_item(MenuItem("Filter users", user_controller.filter, level=2))
        user_page.add_menu_item(MenuItem("Reset filter", user_controller.reset_filter, level=2))
        user_page.add_menu_item(MenuItem("Reset users password (SA)", user_controller.reset_user_password, level=2))
        user_page.add_menu_item(MenuItem("Back", user_page.quit))

        system_logs_page.add_menu_item(MenuItem("Filter logs", log_controller.filter, level=2))
        system_logs_page.add_menu_item(MenuItem("Reset filter", log_controller.reset_filter, level=2))
        system_logs_page.add_menu_item(MenuItem("Create backup", log_controller.backup_system, level=2))
        system_logs_page.add_menu_item(MenuItem("Restore backup", log_controller.restore_system, level=2))
        system_logs_page.add_menu_item(MenuItem("Back", system_logs_page.quit))
        
        return login_page
    
if __name__ == "__main__":
    menu = MenuMaker.define_menu_structure()