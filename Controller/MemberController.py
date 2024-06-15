from datetime import datetime
import random
from Controller.CollectionController import CollectionController
from Model.Member import Member
from Service.MemberService import MemberService
from Controller.InputValidator import InputValidator
from Model.Address import Address

class MemberController(CollectionController):

    _instance = None

    def __init__(self, service : MemberService, input_validator : InputValidator):
        if (MemberController._instance != None):
            return MemberController._instance
        
        self.input_validator = input_validator
        self.service = service
        
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

        # TODO: Implement member_validator
        # if not member_validator.validate_member_id(member_id):
            # self.generate_member_id()
    
        print(f'Generated member ID: {member_id}')
        input('Press enter to continue...')
        return member_id
    
    def add_new_member(self) -> bool:
        # request member data

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

        # check if Adress is valid
        Adress = Address('','','','')

        # check if Street is valid
        while True:
            print("Enter street: ", end="")
            street = input()
            if self.input_validator.validate_member_street(street) is not None:
                break
            print(self.input_validator.get_street_rules())

        Address.set_street_name(Adress, street)

        # check if House number is valid
        while True:
            print("Enter house number: ", end="")
            house_number = input()
            if self.input_validator.validate_member_house_number(house_number) is not None:
                break
            print(self.input_validator.get_house_number_rules())

        Address.set_house_number(Adress, house_number)

        # check if Zipcode is valid
        while True:
            print("Enter zipcode: ", end="")
            zipcode = input()
            if self.input_validator.validate_member_zipcode(zipcode) is not None:
                break
            print(self.input_validator.get_zipcode_rules())

        Address.set_zipcode(Adress, zipcode)
        
        # check if Phone is valid
        while True:
            print("Enter phone: +31 6", end="")
            phone = input()
            phone_number = "+316" + phone
            if self.search(phone_number.lower()) is True:
                print("Cannot add member with same phone number.")
                continue
            if self.input_validator.validate_member_phone(phone) is not None:
                break
            print(self.input_validator.get_phone_rules())
            
        
        # check if Email is valid
        while True:
            print("Enter email: ", end="")
            email = input()
            if self.input_validator.validate_member_email(email) is not None:
                if self.search(email.lower()) is False:
                    break
                else:
                    print("Cannot add member with same email address.")
            else:
                print(self.input_validator.get_email_rules())

        # check if Age is valid
        while True:
            print("Enter age: ", end="")
            age = input()
            if self.input_validator.validate_age(age) is not None:
                break
            print(self.input_validator.get_age_rules())
        
        # check if Gender is valid
        while True:
            print("Gender: \n\t1.Male\n\t2.Female\n\t3.Other\nChoose 1-3: ", end="")
            gender = input()
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


        # check if Weight is valid
        while True:
            print("Enter weight in kg: ", end="")
            weight = input()
            if self.input_validator.validate_weight(weight) is not None:
                break
            print(self.input_validator.get_weight_rules())
        
        # check if Registration_date is valid
        registration_date = datetime.now().date().__str__()
        print(f'Registration date: {registration_date}')
        member_id = self.generate_member_id()

        member = [member_id, first_name, last_name, age, real_gender, weight, Adress.__str__(), email, phone_number, registration_date]

        #Call super.add() to add member to collection
        super().add(member)
        return True

    def update_member(self) -> bool:
        return True

    def remove_member(self):
        return True

    def overview_members(self):
        return True
    
    def reset_user_password(self):
        return True

if (__name__ == "__main__"):
    member_controller = MemberController()
    member_controller.generate_member_id()