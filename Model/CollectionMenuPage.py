
from Model.MenuPage import MenuPage
from Controller.Controllers import controllers


class CollectionMenuPage(MenuPage):
    def __init__(self, name, collection, parent=None):
        super().__init__(name, parent)
        self.collection = collection

    def execute(self, *args):
        super().execute(self.collection, *args)

    