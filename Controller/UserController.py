from Controller.CollectionController import CollectionController
from Controller.LogController import LogController
from Controller.InputValidator import InputValidator
from Service.UserService import UserService
from Service.LogService import LogService
from datetime import datetime
from Controller.DataEncrypter import DataEncrypter
from Model.User import User
import random

class UserController(CollectionController):

    _instance = None

    def __init__(self, service : UserService, input_validator : InputValidator, log_controller : LogController):
        if (UserController._instance != None):
            return UserController._instance
        
        self.input_validator = input_validator
        self.service = service
        self.data_encrypter = DataEncrypter()
        self.log_controller = log_controller
        self.logged_in_user : User = None
        
        super().__init__(service, input_validator)

        self.reset_collection()

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

    
        print(f'Generated user ID: {user_id}')
        input('Press enter to continue...')
        return user_id

    def change_own_password(self):
        while True:
                print('Are you sure you would like to reset your own password? (Y)/(N): ', end='')
                option = input().lower()
                if self.input_validator.detect_sql_injection(option):
                    self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
                if self.input_validator.validate_new_password(option):
                    if (option == 'n'):
                        return True
                    else:
                        break
                else:
                    print(self.input_validator.get_new_password_rules())

        password = self.get_password()
        salt = self.data_encrypter.generate_salt()
        password = self.data_encrypter.hashPassword(password, salt)

        user = [self.logged_in_user.id, self.logged_in_user.username, password, self.logged_in_user.role, self.logged_in_user.first_name, self.logged_in_user.last_name, self.logged_in_user.registration_date, salt]
        self.service.delete(self.logged_in_user.id)
        super().add(user)
        self.logger.create_log(self.logged_in_user.username, f'{user[1]} changed his password', f'Name: {user[5]} {user[6]}, ID: {user[0]}', False, service=LogService())
        print('Password changed')
        input('Press enter to continue...')
        return True
    
    def reset_user_password(self):
        id = self.get_user_id()

        for i, user in enumerate(self.collection):
            if user.id == id:
                user_to_give_password = self.encrypted_collection[i]
                user = self.collection[i]
                break

        while True:
                print('Are you sure you would like to reset users password? (Y)/(N): ', end='')
                option = input().lower()
                if self.input_validator.detect_sql_injection(option):
                    self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
                if self.input_validator.validate_new_password(option):
                    if (option == 'n'):
                        return True
                    else:
                        break
                else:
                    print(self.input_validator.get_new_password_rules())

        password = 'Tijdelijk123!'
        salt = self.data_encrypter.generate_salt()
        password = self.data_encrypter.hashPassword(password, salt)

        user = [user.id, user.username, password, user.role, user.first_name, user.last_name, user.registration_date, salt]
        self.service.delete(user_to_give_password[0])
        super().add(user)
        self.logger.create_log(self.logged_in_user.username, f"{self.logged_in_user.username} changed {user[1]}'s password", f'Name: {user[5]} {user[6]}, ID: {user[0]}', False, service=LogService())
        return True
    
    def add_new_user(self):
        # request consultant/ admin data

        # check if Firstname is valid
        first_name = self.get_first_name()
        # check if Lastname is valid
        last_name = self.get_last_name()
        # check if Username is valid
        user_name = self.get_user_name()

        # check if Password is valid
        password = self.get_password()
        salt = self.data_encrypter.generate_salt()
        password = self.data_encrypter.hashPassword(password, salt)

        # check if Role is valid
        role = self.get_role()

        # check if Registration_date is valid
        registration_date = datetime.now().date().__str__()
        print(f'Registration date: {registration_date}')
        user_id = len(self.collection) + 1

        user = [user_id, user_name, password, role, first_name, last_name, registration_date, salt]

        # Call super.add() to add user to collection
        super().add(user)
        self.logger.create_log(self.logged_in_user.username, f'New {role} is created', f'Name: {first_name.capitalize()} {last_name.capitalize()}, ID: {user_id}', False, service=LogService())
        return True
    
    def get_user_id(self):
        while True:
            print('Enter ID of person to update: ', end='')
            id = input()
            if self.input_validator.detect_sql_injection(id):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_user_id(id):
                break
            else:
                print(self.input_validator.get_user_id_rules())
            
        return id
    
    def reset_collection(self):
        super().reset_collection()
        #ERROR: User is not subscriptable
        # self.collection = [User(*user) for user in self.collection if self.levels[user[3].lower()] >= self.levels[self.logged_in_user.role.lower()]]

        if self.logged_in_user is not None:
            self.collection = [User(*user) for user in self.collection if self.levels[user[3].lower()] >= self.levels[self.logged_in_user.role.lower()]]

        self.collection = [User(*user) for user in self.collection]
    
    def update_user(self):
        id = self.get_user_id()

        for i, user in enumerate(self.collection):
            if user.id == id:
                user_to_update = self.encrypted_collection[i]
                user = User(*self.collection[i])
                break

        while True:
                print('What would you like to update (select one option, 1.Username, 2.First name, 3. Last name): ', end='')
                option = input()
                if self.input_validator.detect_sql_injection(option):
                    self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
                if self.input_validator.validate_user_option(option):
                    break
                else:
                    print(self.input_validator.get_user_option_rules())
        if option == '1':
            username = self.get_user_name()
            first_name = user.first_name
            last_name = user.last_name

        
        elif option == '2':
            username = user.username
            first_name = self.get_first_name()
            last_name = user.last_name
        
        elif option == '3':
            username = user.username
            first_name = user.first_name
            last_name = self.get_last_name()

        user = [user.id, username, user.password, user.role, first_name, last_name, user.registration_date, user.salt]
        self.service.delete(user_to_update[0])
        super().add(user)
        self.logger.create_log(self.logged_in_user.username, f'User is updated', f'Name: {first_name.capitalize()} {last_name.capitalize()}, ID: {user[0]}', False, service=LogService())
        return True

    def remove_user(self):
        while True:
            print('Enter ID of person to delete: ', end='')
            id = input()
            if self.input_validator.detect_sql_injection(id):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_user_id(id):
                break
            else:
                print(self.input_validator.get_user_id_rules())

        for i, user in enumerate(self.collection):
            if user.id == id:
                usertodelete = self.encrypted_collection[i]
                user = self.collection[i]
                break

        self.service.delete(usertodelete[0])
        print('User deleted')
        input('Press enter to continue...')
        self.logger.create_log(self.logged_in_user.username, f'{user.username} is deleted', f'Name: {user.first_name} {user.last_name}, ID: {user.id}', False, service=LogService())
        return True