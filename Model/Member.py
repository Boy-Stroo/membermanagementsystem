from Model.Address import Address


class Member:
    def __init__(self, member_ID: str, first_name : str, last_name : str, address : str, phone : str, email : str, age : str, gender : str, weight : str, registration_date : str):
        self.member_ID = member_ID
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email
        self.age = age
        self.gender = gender
        self.weight = weight
        self.registration_date = registration_date

    def __iter__(self):
        yield self.member_ID
        yield self.first_name
        yield self.last_name
        yield self.address
        yield self.phone
        yield self.email
        yield self.age
        yield self.gender
        yield self.weight
        yield self.registration_date

    def __str__(self) -> str:
        return f'{self.member_ID} {self.first_name} {self.last_name} {self.address} {self.phone} {self.email} {self.age} {self.gender} {self.weight} {self.registration_date}'.lower()
    