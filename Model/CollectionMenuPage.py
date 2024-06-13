
from Controller.DataEncrypter import DataEncrypter
from Controller.UIFormatter import UIFormatter
from Model.MenuPage import MenuPage
from Controller.Controllers import controllers
from Service.Service import Service


class CollectionMenuPage(MenuPage):
    def __init__(self, name: str, service: Service, formatter: UIFormatter, parent=None):
        super().__init__(name, parent)
        self.service = service
        self.encrypted_collection = service.get_all()
        self.collection = [DataEncrypter().decrypt_data(member) for member in self.encrypted_collection]
        self.filtered_collection = []
        self.active_filters = []
        self.formatter = formatter


    def execute(self, *args):
        super().execute(*args)

    def display(self):
        print(self.formatter.display_header(self.name))

        if self.filtered_collection or self.active_filters:
            print(self.formatter.display_filters(self.active_filters))
            print(self.formatter.format_collection(self.filtered_collection, self.service.columns))
        else:
            print(self.formatter.format_collection(self.collection, self.service.columns ))
        
        print(self.formatter.format_menu(self.menu_items))

    def quit(self):
        self.filtered_collection = []
        super().quit()