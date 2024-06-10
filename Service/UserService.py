from Service.Service import Service


class UserService(Service):
    def __init__(self):
        super().__init__()
        self.table = 'users'
        self.columns = {
            'id': 'INTEGER PRIMARY KEY',
            'username': 'TEXT NOT NULL',
            'password': 'TEXT NOT NULL',
            'role': 'TEXT NOT NULL',
            'first_name': 'TEXT NOT NULL',
            'last_name': 'TEXT NOT NULL',
            'registration_date': 'TEXT',
        }