from Model.MenuPage import MenuPage

class UserController:
    def __init__(self):
        pass

    def add_new_user(self, username, password):
        return True

    def update_user(self, username, password):
        return True

    def remove_user(self, username):
        return True

    def change_own_password(self):
        return True
    
    # def overview_users(self, menu_page : MenuPage):
    #     search_term = input('Enter search term: ').lower()
    #     filtered_collection = [x for x in menu_page.collection if x.__str__().lower().find(search_term) != -1]
    #     menu_page.filtered_collection = filtered_collection
    #     return True
    
    def reset_user_password(self):
        return True