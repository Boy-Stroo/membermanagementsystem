from typing import Callable
from Model.MenuComponent import MenuComponent


class MenuItem(MenuComponent):
    def __init__(self, name, action, next_page : MenuComponent = None, arg = None):
        self.name = name
        self.action = action
        self.next_page = next_page if next_page is not None else None
        self.arg = arg

    def display(self):
        print(self.name)

    def execute(self) -> bool:
        if self.action is None and self.next_page is not None:
            return True 

        if self.arg is None:
            return self.action()

        return self.action(self.arg)

    def get_next_page(self):
        return self.next_page
    