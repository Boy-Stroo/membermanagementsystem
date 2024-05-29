import os

from Model.MenuComponent import MenuComponent


class MenuPage(MenuComponent):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.menu_items = []


    def execute(self, *args):
        os.system('cls' if os.name == 'nt' else 'clear')

        print(self.name)

        for index, item in enumerate(self.menu_items, start=1):
            print(f"{index}. {item.name}")

        option = self.get_input()

        if self.menu_items[option - 1].execute(*args):
            next_page : MenuPage = self.menu_items[option - 1].get_next_page()
            if next_page is not None:
                next_page.set_parent(self)
                next_page.execute(*args)
        
    

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
        self.execute()

    def set_parent(self, parent):
        self.parent = parent