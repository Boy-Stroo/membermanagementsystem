
from Controller.DataEncrypter import DataEncrypter
from Controller.UIFormatter import UIFormatter
from Model.MenuPage import MenuPage
from Controller.Controllers import controllers
from Service.Service import Service


class CollectionMenuPage(MenuPage):
    def __init__(self, name: str, service: Service, formatter: UIFormatter, parent=None):
        super().__init__(name, parent)
        self.service = service
        self.collection = [DataEncrypter().decrypt_data(member) for member in service.get_all()]
        self.formatter = formatter

    def execute(self, *args):
        super().execute(*args)

    def display(self):
        print(self.formatter.display_header(self.name))
        print(self.formatter.format_collection(self.collection, self.service.columns ))
        print(self.formatter.format_menu(self.menu_items))
