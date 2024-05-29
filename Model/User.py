from Model.Role import Role


class User:
    def __init__(self, id, username, password, role: Role):
        self.id = id
        self.username = username
        self.password = password
        self.role = role if isinstance(role, Role) else Role(role)

    def __str__(self):
        return f'{self.id} {self.username} {self.role}'
    