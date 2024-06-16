from Service.Service import Service


class UserService(Service):
    def __init__(self):
        super().__init__()
        self.table = 'users'
        self.columns = ['id', 'username', 'password', 'role', 'first_name', 'last_name', 'registration_date', 'salt']
