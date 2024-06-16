from Controller.DataEncrypter import DataEncrypter
from Controller.InputValidator import InputValidator
from Service.Service import Service
from Service.LogService import LogService
from Controller.Logger import Logger


class CollectionController:

    def __init__(self, service : Service, input_validator : InputValidator):
        self.service = service
        self.encrypted_collection = service.get_all()
        self.collection = [DataEncrypter().decrypt_data(member) for member in self.encrypted_collection]
        self.filtered_collection = []
        self.active_filters = []
        self.input_validator = input_validator
        self.logger = Logger()
        self.levels = {
            'super admin': 1,
            'system admin': 2,
            'consultant': 3
        }
        self.date_accessed = Logger().read_date()

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
        self.collection.sort(key=lambda x: x[0])

        if self.active_filters != []:
            self.filtered_collection = [x for x in self.collection if x.__str__().lower().find(self.active_filters[-1]) != -1]
        

        return True
    
    def search(self, search_term: str) -> bool:
        return [x for x in self.collection if x.__str__().lower().find(search_term) != -1] != []
    
    def update(self, id : str, paramtochange : str, new_value : str) -> bool:
        return True

    def delete():
        return True

    def add(self, entity):
        self.collection.append(entity)
        self.encrypted_collection.append(DataEncrypter().encrypt_data_list(entity))
        self.service.create(DataEncrypter().encrypt_data_list(entity))

    def get_first_name(self):
        while True:
            print("Enter first name: ", end="")
            first_name = input()
            if self.input_validator.detect_sql_injection(first_name):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            
            if self.input_validator.validate_first_name(first_name) is not None:
                break
            print(self.input_validator.get_first_name_rules())
        
        return first_name

    def get_last_name(self):
        while True:
            print("Enter last name: ", end="")
            last_name = input()
            if self.input_validator.detect_sql_injection(last_name):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_last_name(last_name) is not None:
                break
            print(self.input_validator.get_last_name_rules())
        
        return last_name
    
    def find_in_collection(self, search_term, index):
        return [x for x in self.collection if x[index].lower().find(search_term) != -1]
    
    def get_user_name(self):
        while True:
            print("Enter username: ", end="")
            user_name = input()
            if self.input_validator.detect_sql_injection(user_name):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_user_name(user_name) is not None:
                if self.find_in_collection(user_name.lower(), 1) == []:
                    break
                else:
                    print("Cannot add member with same Username.")
            else:
                print(self.input_validator.get_user_name_rules())

        return user_name
    

    def get_email(self):
        while True:
            print("Enter email: ", end="")
            email = input()
            if self.input_validator.detect_sql_injection(email):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_member_email(email) is not None:
                if self.find_in_collection(email.lower(), 7) == []:
                    break
                else:
                    print("Cannot add member with same email address.")
            else:
                print(self.input_validator.get_email_rules())
    
        return email

    def get_role(self):
        while True:
            print("Enter role \n\t1.Consultant\n\t2.System admin\nChoose 1-2: ", end="")
            role = input()
            if self.input_validator.detect_sql_injection(role):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_role(role) is not None:
                break
            print(self.input_validator.get_role_rules())
        real_role = ''
        match (role):
            case "1":
                real_role = "Consultant"
            case "2":
                real_role = "System admin"
        
        return real_role
    
    def get_password(self):
        while True:
            print("Enter password: ", end="")
            password = input()
            if self.input_validator.detect_sql_injection(password):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_password(password) is not None:
                break
            print(self.input_validator.get_password_rules())

        return password
    
    def get_street(self):
        while True:
            print("Enter street: ", end="")
            street = input()
            if self.input_validator.detect_sql_injection(street):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_member_street(street) is not None:
                break
            print(self.input_validator.get_street_rules())
    
        return street
    
    def get_house_number(self):
        while True:
            print("Enter house number: ", end="")
            house_number = input()
            if self.input_validator.detect_sql_injection(house_number):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_member_house_number(house_number) is not None:
                break
            print(self.input_validator.get_house_number_rules())
        
        return house_number
    
    def get_zipcode(self):
        while True:
            print("Enter zipcode: ", end="")
            zipcode = input()
            if self.input_validator.detect_sql_injection(zipcode):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_member_zipcode(zipcode) is not None:
                zipcode = zipcode.upper()
                break
            print(self.input_validator.get_zipcode_rules())
    
        return zipcode
    
    def get_phone_number(self):
        while True:
            print("Enter phone: +31 6", end="")
            phone = input()
            if self.input_validator.detect_sql_injection(phone):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            phone_number = "+316" + phone
            if self.find_in_collection(phone_number, 8) != []:
                print("Cannot add member with same phone number.")
                continue
            if self.input_validator.validate_member_phone(phone) is not None:
                break
            print(self.input_validator.get_phone_rules())
        
        return phone_number
    
    def get_age(self):
        while True:
            print("Enter age: ", end="")
            age = input()
            if self.input_validator.detect_sql_injection(age):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_age(age) is not None:
                break
            print(self.input_validator.get_age_rules())

        return age
    
    def get_gender(self):
        while True:
            print("Gender: \n\t1.Male\n\t2.Female\n\t3.Other\nChoose 1-3: ", end="")
            gender = input()
            if self.input_validator.detect_sql_injection(gender):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_gender(gender) is not None:
                break
            print(self.input_validator.get_gender_rules())
        real_gender = ''
        match (gender):
            case "1":
                real_gender = "Male"
            case "2":
                real_gender = "Female"
            case "3":
                real_gender = "Other"
            case _:
                real_gender = "Other"
        
        return real_gender
    
    def get_weight(self):
        while True:
            print("Enter weight in kg: ", end="")
            weight = input()
            if self.input_validator.detect_sql_injection(weight):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_weight(weight) is not None:
                break
            print(self.input_validator.get_weight_rules())
        
        return weight

if "__main__" == __name__:
    print("CollectionController.py is being run directly.")