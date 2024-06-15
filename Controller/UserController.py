from Controller.CollectionController import CollectionController
from Controller.InputValidator import InputValidator
from Service.UserService import UserService
from datetime import datetime
import random

class UserController(CollectionController):

    _instance = None

    def __init__(self, service : UserService, input_validator : InputValidator):
        if (UserController._instance != None):
            return UserController._instance
        
        self.input_validator = input_validator
        self.service = service
        
        super().__init__(service, input_validator)

    def generate_user_id(self) -> str:
        year = datetime.now().year.__str__()[2:]
        intyear = int(year)

        random_numbers = list()
        # Add first to numbers of the year
        random_numbers.append(int(year[0]))
        random_numbers.append(int(year[1]))
        
        # Add 7 random numbers
        for i in range(0, 7):
            random_numbers.append(random.randint(0, 9))
        
        # Calculate and add checksum
        checksum = sum(random_numbers) % 10
        random_numbers.append(checksum)

        user_id = ''.join(map(str, random_numbers))

        # TODO: Implement user_validator
        # if not user_validator.validate_user_id(user_id):
            # self.generate_user_id()
    
        print(f'Generated user ID: {user_id}')
        input('Press enter to continue...')
        return user_id

    def change_own_password(self):
        return True
    
    def reset_user_password(self):
        return True
    
    def add_new_user(self):
        # request consultant/ admin data

        # check if Firstname is valid
        while True:
            print("Enter first name: ", end="")
            first_name = input()
            if self.input_validator.validate_first_name(first_name) is not None:
                break
            print(self.input_validator.get_first_name_rules())

        # check if Lastname is valid
        while True:
            print("Enter last name: ", end="")
            last_name = input()
            if self.input_validator.validate_last_name(last_name) is not None:
                break
            print(self.input_validator.get_last_name_rules())

        # check if Username is valid
        while True:
            print("Enter username: ", end="")
            user_name = input()
            if self.input_validator.validate_user_name(user_name) is not None:
                if self.search(user_name.lower()) is False:
                    break
                else:
                    print("Cannot add member with same Username.")
            else:
                print(self.input_validator.get_user_name_rules())

        # check if Password is valid
        while True:
            print("Enter password: ", end="")
            password = input()
            if self.input_validator.validate_password(password) is not None:
                break
            print(self.input_validator.get_password_rules())

        # check if Role is valid
        while True:
            print("Enter role \n\t1.Consultant\n\t2.System admin\nChoose 1-2: ", end="")
            role = input()
            if self.input_validator.validate_role(role) is not None:
                break
            print(self.input_validator.get_role_rules())
        real_role = ''
        match (role):
            case "1":
                real_role = "Consultant"
            case "2":
                real_role = "System admin"

        # check if Registration_date is valid
        registration_date = datetime.now().date().__str__()
        print(f'Registration date: {registration_date}')
        user_id = self.generate_user_id()

        user = [user_id, user_name, password, real_role, first_name, last_name, registration_date]

        # Call super.add() to add user to collection
        super().add(user)
        return True
    
    def update_user(self):  
        return True
    
    def remove_user(self):  
        return True