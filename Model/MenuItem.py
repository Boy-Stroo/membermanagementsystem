from Model.MenuComponent import MenuComponent


class MenuItem(MenuComponent):
    def __init__(self, name, action, next_page : MenuComponent = None, level=3, *args):
        self.name = name
        self.action = action
        self.next_page = next_page if next_page is not None else None
        self.level = level
        self.args = args

    def display(self):
        print(self.name)

    def execute(self) -> bool:
        # if there is no action, but there is a next page, go to the next page
        if self.action is None and self.next_page is not None:
            return True 

        return self.action(*self.args)
        # if the
        # if self.arg is None:
        #     return self.action()

        # return self.action(self.arg)

    def get_next_page(self):
        return self.next_page
    