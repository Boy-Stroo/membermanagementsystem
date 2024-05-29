
from Controller.LoginController import LoginController
from Controller.MemberController import MemberController


class Controllers:
    # singleton
    def __init__(self):
        self.login_controller = LoginController()
        self.member_controller = MemberController()

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Controllers, cls).__new__(cls)
        return cls.instance


    def get_login_controller(self):
        return self.login_controller




controllers = Controllers()