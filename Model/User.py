from Model.Role import Role


class User:
    def __init__(self, id, username, password, role, first_name, last_name, registration_date, salt):
        self.id = id
        self.username = username
        self.password = password
        self.role = role
        self.first_name = first_name
        self.last_name = last_name
        self.registration_date = registration_date
        self.salt = salt

    #make iterable
    def __iter__(self):
        yield self.id
        yield self.username
        yield self.password
        yield self.role
        yield self.first_name
        yield self.last_name
        yield self.registration_date
        yield self.salt

    def __str__(self) -> str:
        return f'{self.id} {self.username} {self.first_name} {self.last_name} {self.registration_date} {self.role}'