from datetime import datetime
import random
from Controller.CollectionController import CollectionController
from Model.Member import Member
from Service.MemberService import MemberService
from Controller.InputValidator import InputValidator
from Model.Address import Address
from Controller.DataEncrypter import DataEncrypter
from Controller.LogController import LogController
from Controller.UserController import UserController
from Service.LogService import LogService

class MemberController(CollectionController):

    _instance = None

    def __init__(self, service : MemberService, input_validator : InputValidator, log_controller: LogController, user_controller: UserController):
        if (MemberController._instance != None):
            return MemberController._instance
        
        self.input_validator = input_validator
        self.service = service
        self.data_encrypter = DataEncrypter()
        self.log_controller = log_controller
        self.user_controller = user_controller

        
        super().__init__(service, input_validator)

    def generate_member_id(self) -> str:
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

        member_id = ''.join(map(str, random_numbers))

        return member_id
    
    def add_new_member(self) -> bool:
        # request member data

        # check if Firstname is valid
        first_name = self.get_first_name()
        # check if Lastname is valid
        last_name = self.get_last_name()
        # check if Adress is valid
        Adress = Address('','','','')
        # check if Street is valid
        street = self.get_street()
        Address.set_street_name(Adress, street)
        # check if House number is valid
        house_number = self.get_house_number()
        Address.set_house_number(Adress, house_number)
        # check if Zipcode is valid
        zipcode = self.get_zipcode()
        Address.set_zipcode(Adress, zipcode)
        # check if Phone is valid
        phone_number = self.get_phone_number()
        # check if Email is valid
        email = self.get_email()
        # check if Age is valid
        age = self.get_age()
        # check if Gender is valid
        gender = self.get_gender()
        # check if Weight is valid
        weight = self.get_weight()
        
        # check if Registration_date is valid
        registration_date = datetime.now().date().__str__()
        print(f'Registration date: {registration_date}')
        member_id = self.generate_member_id()

        #           0          1          2           3      4       5       6                7        8             9
        member = [member_id, first_name, last_name, age, gender, weight, Adress.__str__(), email, phone_number, registration_date]

        #Call super.add() to add member to collection
        super().add(member)
        self.logger.create_log(self.user_controller.logged_in_user.username, 'New member is created', f'Name: {first_name.capitalize()} {last_name.capitalize()}, ID: {member_id}', False, service=LogService())
        return True

    def update_member(self) -> bool:
        while True:
            print('Enter ID of person to update: ', end='')
            id = input()
            if self.input_validator.detect_sql_injection(id):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_user_id(id):
                break
            else:
                print(self.input_validator.get_user_id_rules())

        member_to_update = None
        for i, member in enumerate(self.collection):
            if member[0] == id:
                encrypted_member_to_update = self.encrypted_collection[i]
                member_to_update = self.collection[i]
                break
        
        if member_to_update == None:
            print('Member not found')
            input('Press enter to continue...')
            return False

        while True:
                print('What would you like to update (select one option, \n\t1.First name, \n\t2.Last name, \n\t3.Age, \n\t4.Gender, \n\t5.Weight, \n\t6.Address, \n\t7.Email, \n\t8.Phone number):\n\t ', end='')
                option = input()
                if self.input_validator.detect_sql_injection(option):
                    self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
                if self.input_validator.validate_member_option(option):
                    break
                else:
                    print(self.input_validator.get_member_option_rules())

        #First name
        if option == '1':
            first_name = self.get_first_name()
            last_name = member_to_update[2]
            age = member_to_update[3]
            gender = member_to_update[4]
            weight = member_to_update[5]
            address = member_to_update[6]
            email = member_to_update[7]
            phone_number = member_to_update[8]
            
        #Last name
        elif option == '2':
            first_name = member_to_update[1]         
            last_name = self.get_last_name()
            age = member_to_update[3]
            gender = member_to_update[4]
            weight = member_to_update[5]
            address = member_to_update[6]
            email = member_to_update[7]
            phone_number = member_to_update[8]

        #Age        
        elif option == '3':
            first_name = member_to_update[1]         
            last_name = member_to_update[2]
            age = self.get_age()
            gender = member_to_update[4]
            weight = member_to_update[5]
            address = member_to_update[6]
            email = member_to_update[7]
            phone_number = member_to_update[8]

        #Gender
        elif option == '4':
            first_name = member_to_update[1]
            last_name = member_to_update[2]
            age = member_to_update[3]
            gender = self.get_gender()
            weight = member_to_update[5]
            address = member_to_update[6]
            email = member_to_update[7]
            phone_number = member_to_update[8]

        #Weight
        elif option == '5':
            first_name = member_to_update[1]
            last_name = member_to_update[2]
            age = member_to_update[3]
            gender = member_to_update[4]
            weight = self.get_weight()
            address = member_to_update[6]
            email = member_to_update[7]
            phone_number = member_to_update[8]

        #Address
        elif option == '6':
            first_name = member_to_update[1]
            last_name = member_to_update[2]
            age = member_to_update[3]
            gender = member_to_update[4]
            weight = member_to_update[5]
            street = self.get_street()
            house_number = self.get_house_number()
            zipcode = self.get_zipcode()
            address = Address(street, house_number, zipcode)
            address = address.__str__()
            email = member_to_update[7]
            phone_number = member_to_update[8]

        #Email
        elif option == '7':
            first_name = member_to_update[1]    
            last_name = member_to_update[2]
            age = member_to_update[3]
            gender = member_to_update[4]
            weight = member_to_update[5]
            address = member_to_update[6]
            email = self.get_email()
            phone_number = member_to_update[8]

        #Phone number
        elif option == '8':
            first_name = member_to_update[1]
            last_name = member_to_update[2]
            age = member_to_update[3]
            gender = member_to_update[4]
            weight = member_to_update[5]
            address = member_to_update[6]
            email = member_to_update[7]
            phone_number = self.get_phone_number()
        
        member = [member_to_update[0], first_name, last_name, age, gender, weight, address, email, phone_number, member_to_update[9]]
        self.service.delete(encrypted_member_to_update[0])
        super().add(member)
        self.logger.create_log(self.user_controller.logged_in_user.username, 'Member is updated', f'Name: {first_name.capitalize()} {last_name.capitalize()}, ID: {member_to_update[0]}', False, service=LogService())
        return True

    def reset_collection(self):
        self.collection = [Member(*member) for member in self.collection]
        super().reset_collection()

    def remove_member(self):
        while True:
            print('Enter ID of person to delete: ', end='')
            id = input()
            if self.input_validator.detect_sql_injection(id):
                self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            if self.input_validator.validate_user_id(id):
                break
            else:
                print(self.input_validator.get_user_id_rules())

        for i, member in enumerate(self.collection):
            if member[0] == id:
                member_to_delete = self.encrypted_collection[i]
                member = self.collection[i]
                break

        self.service.delete(member_to_delete[0])
        print('Member deleted')
        input('Press enter to continue...')
        self.logger.create_log(self.user_controller.logged_in_user.username, 'Member is deleted', f'Name: {member[1]} {member[2]} ID: {member[0]}', False, service=LogService())
        return True

if (__name__ == "__main__"):
    member_controller = MemberController()
    member_controller.generate_member_id()