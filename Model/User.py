from Model.Role import Role


class User:
    def __init__(self, id, username, password, role: Role, first_name, last_name, registration_date):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.registration_date = registration_date
        self.role = role if isinstance(role, Role) else Role(role)        

    def __str__(self) -> str:
        return f'{self.id} {self.username} {self.first_name} {self.last_name} {self.registration_date} {self.role}'