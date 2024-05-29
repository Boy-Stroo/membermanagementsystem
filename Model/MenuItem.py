from typing import Callable
from Model.MenuComponent import MenuComponent


class MenuItem(MenuComponent):
    def __init__(self, name, action : Callable[[], bool], next_page : MenuComponent = None):
        self.name = name
        self.action = action
        self.next_page = next_page if next_page is not None else None

    def display(self):
        print(self.name)

    def execute(self, *args) -> bool:
        return self.action(*args)

    def get_next_page(self):
        return self.next_page
    