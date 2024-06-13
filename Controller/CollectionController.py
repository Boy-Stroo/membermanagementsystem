from Model.MenuPage import MenuPage

class CollectionController:
    def filter(self, menu_page : MenuPage):
        search_term = input('Enter search term: ').lower()
        if menu_page.filtered_collection == []:
            filtered_collection = [x for x in menu_page.collection if x.__str__().lower().find(search_term) != -1]
        else:
            filtered_collection = [x for x in menu_page.filtered_collection if x.__str__().lower().find(search_term) != -1]
        
        menu_page.filtered_collection = filtered_collection
        return True
