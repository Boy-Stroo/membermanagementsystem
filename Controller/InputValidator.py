# import DataEncrypter
# import Logger
import re

class InputValidator:
    # def __init__(self, data_encrypter: DataEncrypter, logger: Logger) -> None:

    def validate_input(self, input):
        pass

    def validate_username(self, username):
        regex = r"^[a-zA-Z0-9_'.]{8,10}"
        return re.match(regex, username)

    def get_username_rules(self):
        return "Username must be 8-10 characters long and can only contain letters, numbers, underscores, apostrophes, and periods."

    def validate_password(self, password):
        regex = r"^[a-zA-Z~!@#$%&_\-+=`|\\(){}[\]:;'<>,.?\/]{12,30}"
        return re.match(regex, password)

    def validate_first_name(self, name):
        regex = r"^[A-Za-zÀ-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ', '-]{1,29}$"
        return re.match(regex, name)
    
    def get_first_name_rules(self):
        return "First name must start with a letter and can only contain letters, apostrophes, hyphens, and spaces."
    
    def validate_last_name(self, name):
        regex = r"^[A-Za-zÀ-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ',. '-]{1,29}$"
        return re.match(regex, name)

    def get_last_name_rules(self):
        return "Last name must start with a letter and can only contain letters, apostrophes, hyphens, periods, and spaces."
    
    def validate_member_email(self, email):
        regex = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$'
        return re.match(regex, email)
    
    def get_email_rules(self):
        return "Incorrect email format. Please enter a valid email address."
        
    def validate_member_phone(self, phone_number):
        regex = r"^\d{8}$"
        return re.match(regex, phone_number)
    
    def get_phone_rules(self):
        return "Phone number (+31 6) must be extended by 8 digits and can only contain numbers."
    
    def validate_member_street(self, street):
        regex = r"^[A-Za-zÀ-ÖØ-öø-ÿ][A-Za-zÀ-ÖØ-öø-ÿ',. '-]{1,29}$"
        return re.match(regex, street)
    
    def get_street_rules(self):
        return "Street name must start with a letter and can only contain letters, apostrophes, hyphens, periods, and spaces."
    
    def validate_member_house_number(self, house_number):
        regex = r"^\d{1,5}$"
        return re.match(regex, house_number)
    
    def get_house_number_rules(self):
        return "House number must be a number between 1 and 5 digits long."
    
    def validate_member_zipcode(self, zipcode):
        regex = r"^\d{4}[A-Za-z]{2}$"
        return re.match(regex, zipcode)
    
    def get_zipcode_rules(self):
        return "Zipcode must be 4 digits followed by 2 letters."
    
    def validate_gender(self, gender):
        regex = r"^[1-3]$"
        return re.match(regex, gender)

        
    def get_gender_rules(selft):
        return "Enter 1, 2 or 3"
    
    def validate_age(self, age):
        regex = r"^\d{1,3}$"
        return re.match(regex, age)
    
    def get_age_rules(self):
        return "Age must be a number between 1 and 3 digits long."
    
    def validate_weight(self, weight):
        regex = r"^\d{1,3}$"
        return re.match(regex, weight)
    
    def get_weight_rules(self):
        return "Weight must be a number between 1 and 3 digits long in kg's."