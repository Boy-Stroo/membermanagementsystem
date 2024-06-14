import DataEncrypter
import Logger
import re

class InputValidator:
    # def __init__(self, data_encrypter: DataEncrypter, logger: Logger) -> None:

    def validate_input(self, input):
        pass

    def validate_username(self, username):
        regex = "^[a-zA-Z0-9_'.]{8,10}"
        return re.match(regex, username)

    def validate_password(self, password):
        regex = r"^[a-zA-Z~!@#$%&_\-+=`|\\(){}[\]:;'<>,.?\/]{12,30}"
        return re.match(regex, password)

    def validate_first_or_last_name(self, name):
        regex = r"/^[a-z ,.'-]+$/i"
        return re.match(regex, name)
    
    def validate_member_email(self, email):
        regex = r"^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$"
        return re.match(regex, email)
    
    def validate_member_phone(self, phone_number):
        regex = r"^\d{8}"
        return re.match(regex, phone_number)