from tabulate import tabulate

class UIFormatter():

    def __init__(self):
        pass

    def display_header(self, title: str):
        return f"{title}"


    def format_menu(self, menu_items: list):
        menu = ''
        for index, item in enumerate(menu_items, start=1):
            menu += f"{index}. {item.name}\n"
        
        return menu

    def format_collection(self, collection: list, headers):
        return tabulate(collection, headers=headers, tablefmt='rounded_grid')
    
    def display_filters(self, filters: list):
        return f"Active filters: {', '.join(filters)}"

