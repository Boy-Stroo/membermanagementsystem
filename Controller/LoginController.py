from Controller.UserController import UserController
from Controller.LogController import LogController
from Controller.InputValidator import InputValidator
from Service.LogService import LogService
import ast
from Controller.Logger import Logger
from Model.User import User


class LoginController:
    def __init__(self, user_controller: UserController, log_controller: LogController, input_validator: InputValidator):
        self.user_controller = user_controller
        self.log_controller = log_controller
        self.incorrect_login_attempts = 0
        self.input_validator = input_validator
        self.logger = Logger()

    def check_login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check for SQL injection in username and password
        if self.input_validator.detect_sql_injection(username) or self.input_validator.detect_sql_injection(password):
            self.logger.create_log("", "SQL injection attempt detected", "", True, service=LogService())
            return False
        

        for user in self.user_controller.collection:
            my_user: User = User(*user)
            if my_user.username == username:
                salt = my_user.salt
                cleaned_salt = ast.literal_eval(salt)
                hashed_password = self.user_controller.data_encrypter.hashPassword(password, cleaned_salt)
                if my_user.password == hashed_password:
                    print("Login successful")
                    self.logger.create_log(username, f"[{my_user.role}] {my_user.username} successfully logged in", "", False, service=LogService())
                    self.incorrect_login_attempts = 0
                    self.user_controller.logged_in_user = User(*user)
                    return True
                else:
                    self.incorrect_login_attempts += 1
                    if self.incorrect_login_attempts == 3:
                        print("Too many incorrect login attempts, exiting program")
                        self.logger.create_log("", "Too many incorrect login attempts, exiting program", f"'{username}' tried to login too many times", True, service=LogService())
                        # Ook nog logger callen om een melding te sturen naar de admins.
                        exit()
                    input("Incorrect username or password... Press enter to try again.")
                    self.logger.create_log(username, "Incorrect username or password", "", False, service=LogService())
                    return False
        else:
            self.incorrect_login_attempts += 1
            if self.incorrect_login_attempts == 3:
                print("Too many incorrect login attempts, exiting program")
                self.logger.create_log("", "Too many incorrect login attempts, exiting program", f"'{username}' tried to login too many times", True, service=LogService())
                # Ook nog logger callen om een melding te sturen naar de admins.
                exit()
            input("Incorrect username or password... Press enter to try again.")
            self.logger.create_log(username, "Incorrect username or password", "", False, service=LogService())
            return False

        