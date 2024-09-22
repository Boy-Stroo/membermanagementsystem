import os

from Model.MenuComponent import MenuComponent
from Controller.UserController import UserController
from Model.MenuItem import MenuItem
from typing import List
from Controller.LogController import LogController
from Service.LogService import LogService
from Controller.Logger import Logger
from Controller.InputValidator import InputValidator


class MenuPage(MenuComponent):
    def __init__(self, name, formatter, user_controller, parent=None):
        self.name = name
        self.parent = parent
        self.formatter = formatter
        self.user_controller : UserController = user_controller
        self.menu_items : List[MenuItem] = []
        self.active_menu_items = []
        self.levels = {
            'super admin': 1,
            'system admin': 2,
            'consultant': 3
        }
        self.logger = Logger()
        self.log_service = LogService()
        self.input_validator = InputValidator()


    def execute(self, *args):
        os.system('cls' if os.name == 'nt' else 'clear')

        date_accessed = self.logger.read_date()

        suspicious_logs = LogController(self.log_service, self.input_validator).get_suspicious_logs(date_accessed)
        if suspicious_logs != [] and self.name != "Login":
            if "admin" in self.user_controller.logged_in_user.role:
                print(f"Suspicious logs found: {len(suspicious_logs)}")
        
        if self.name == "System Logs":
            self.logger.write_date()


        if self.user_controller.logged_in_user :
            self.active_menu_items = [x for x in self.menu_items if x.level >= self.levels[self.user_controller.logged_in_user.role.lower()]]

        self.display()

        option = self.get_input()

        

        if self.menu_items[option - 1].execute():
            next_page : MenuPage = self.menu_items[option - 1].get_next_page()
            if next_page :
                next_page.set_parent(self)
                next_page.execute(*args)
            else:
                self.execute(*args)
        else:
            self.execute(*args)
        
    

    def get_input(self):
        option = input("Enter the number of the option you would like to select: ")

        if not option.isdigit():
            print("Invalid input. Please enter a number.")
            return self.get_input()

        option = int(option)

        if option < 1 or option > len(self.menu_items):
            print("Invalid input. Please enter a valid option.")
            return self.get_input()
        
        return option

    def add_menu_item(self, menu_item):
        self.menu_items.append(menu_item)

    def quit(self):
        if self.parent is None:
            print("Goodbye!")
            exit()
        else:
            self.parent.execute()

    def display(self):
        print(self.formatter.display_header(self.name))
        if self.user_controller.logged_in_user is None:
            print(self.formatter.format_menu(self.menu_items))
        else:
            print(self.formatter.format_menu(self.active_menu_items))

    def set_parent(self, parent):
        self.parent = parent