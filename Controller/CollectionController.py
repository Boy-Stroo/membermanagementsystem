from Controller.DataEncrypter import DataEncrypter
from Controller.InputValidator import InputValidator
from Service.Service import Service


class CollectionController:

    def __init__(self, service : Service, input_validator):
        self.service = service
        self.encrypted_collection = service.get_all()
        self.collection = [DataEncrypter().decrypt_data(member) for member in self.encrypted_collection]
        self.filtered_collection = []
        self.active_filters = []
        self.input_validator = input_validator

    def filter(self):
        search_term = input('Enter search term: ').lower() # TODO move to an input validator

        if self.filtered_collection == []:
            filtered_collection = [x for x in self.collection if x.__str__().lower().find(search_term) != -1]
        else:
            filtered_collection = [x for x in self.filtered_collection if x.__str__().lower().find(search_term) != -1]
        
        self.filtered_collection = filtered_collection
        self.active_filters.append(search_term)
        return True
        

    def reset_filter(self):
        self.filtered_collection = []
        self.active_filters = []
        return True
    
    def reset_collection(self):
        self.encrypted_collection = self.service.get_all()
        self.collection = [DataEncrypter().decrypt_data(member) for member in self.encrypted_collection]
        if self.active_filters != []:
            self.filtered_collection = [x for x in self.collection if x.__str__().lower().find(self.active_filters[-1]) != -1]
        
        return True
    
    def search(self, search_term: str) -> bool:
        return [x for x in self.collection if x.__str__().lower().find(search_term) != -1] != []
    
    def update():
        return True

    def delete():
        return True

    def add(self, entity):
        self.collection.append(entity)
        self.encrypted_collection.append(DataEncrypter().encrypt_data(entity))
        self.service.create(DataEncrypter().encrypt_data(entity))


if "__main__" == __name__:
    print("CollectionController.py is being run directly.")