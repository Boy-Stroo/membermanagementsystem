# import DataEncrypter
# import Logger
import re

class InputValidator:
    # def __init__(self, log_controller):
        # self.log_controller = log_controller

    def detect_sql_injection(self, input_string: str) -> bool:
        # Common SQL injection patterns
        sql_injection_patterns = [
            r"(?i)(\b(SELECT|UNION|INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|TRUNCATE|REPLACE|EXEC|SHOW|DESCRIBE|USE)\b)",
            r"(?i)(--|#|\/\*|\*\/|;)"
        ]
        for pattern in sql_injection_patterns:
            if re.search(pattern, input_string):
                return True
        return False

    def validate_input(self, input):
        pass

    def validate_user_name(self, username):
        regex = r"^[a-zA-Z_][a-zA-Z0-9_'.]{7,9}$"
        return re.match(regex, username)

    def get_user_name_rules(self):
        return "Username must start with a letter or underscore and can only contain letters, numbers, underscores, apostrophes, and periods and must be 8-10 characters long."

    def validate_password(self, password):
        regex = r"^[a-zA-Z0-9~!@#$%&_\-+=`|\\(){}[\]:;'<>,.?\/]{12,30}$"
        return re.match(regex, password)
    
    def get_password_rules(self):
        return "Password must be 12-30 characters long and must contain at least one uppercase letter, one lowercase letter, one number, and one special character."

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
    
    def validate_role(self, role):
        regex = r"^[1-2]$"
        return re.match(regex, role)
    
    def get_role_rules(self):
        return "Enter 1 or 2"
    
    def validate_user_id(self, user_id):
        regex = r"^\d{1,10}$"
        return re.match(regex, user_id)
    
    def get_user_id_rules(self):
        return "User ID must be a number between 1 and 10 digits long."
    
    def validate_user_option(self, option):
        regex = r"^[1-3]$"
        return re.match(regex, option)
    
    def get_user_option_rules(self):
        return "Enter 1, 2 or 3"
    
    def validate_member_option(self, option):
        regex = r"^[1-8]$"
        return re.match(regex, option)
    
    def get_member_option_rules(self):
        return "Enter 1-8"
    
    def validate_new_password(self, option):
        regex = r"^[yYnN]$"
        return re.match(regex, option)
    
    def get_new_password_rules(self):
        return "Enter Y or N"