from Service.Service import Service


class UserService(Service):
    def __init__(self):
        super().__init__()
        self.table = 'users'
        self.columns = ['id', 'username', 'password', 'role', 'first_name', 'last_name', 'registration_date']

    def get_salt(self, username: str) -> str:
        return self.get_by_column('username', username, 'salt')