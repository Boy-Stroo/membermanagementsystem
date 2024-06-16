
from Controller.DataEncrypter import DataEncrypter
from Controller.UIFormatter import UIFormatter
from Model.MenuPage import MenuPage
from Controller.CollectionController import CollectionController
from Service.Service import Service
from Service.LogService import LogService
from Controller.Logger import Logger
from Controller.InputValidator import InputValidator
from Controller.LogController import LogController


class CollectionMenuPage(MenuPage):
    def __init__(self, name: str, controller : CollectionController, formatter: UIFormatter, user_controller, parent=None):
        super().__init__(name, parent, user_controller)
        self.controller = controller
        self.formatter = formatter
        self.logger = Logger()
        self.log_controller = LogController(LogService(), InputValidator())
        self.date_accessed = self.logger.read_date()


    def execute(self, *args):
        self.controller.reset_collection()
        super().execute(*args)


    def display(self):
        print(self.formatter.display_header(self.name))

        if self.controller.filtered_collection or self.controller.active_filters:
            print(self.formatter.display_filters(self.controller.active_filters))
            print(self.formatter.format_collection(self.controller.filtered_collection, self.controller.service.columns))
        else:
            print(self.formatter.format_collection(self.controller.collection, self.controller.service.columns ))
        
        print(self.formatter.format_menu(self.menu_items))

    def quit(self):
        self.controller.filtered_collection = []
        super().quit()
