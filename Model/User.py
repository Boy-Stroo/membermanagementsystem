from enum import Enum

class User:
    def __init__(self, id, username, password, role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f'{self.id} {self.username} {self.role}'
    
class Role(Enum):
    SUPERADMIN = 1
    ADMIN = 2
    CONSULTANT = 3