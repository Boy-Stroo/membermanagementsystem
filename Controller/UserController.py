from Controller.CollectionController import CollectionController

class UserController(CollectionController):

    _instance = None
    def __init__(self, service, input_validator):
        if UserController._instance is not None:
            return UserController._instance
        UserController._instance = self
        super().__init__(service, input_validator)

    def change_own_password(self):
        return True
    
    def reset_user_password(self):
        return True
    
    def add_new_user(self):
        return True
    
    def update_user(self):  
        return True
    
    def remove_user(self):  
        return True