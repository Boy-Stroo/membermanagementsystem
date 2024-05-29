from Model.Address import Address


class Member:
    def __init__(self, member_ID: str, first_name : str, last_name : str, address : Address, phone : str, email : str):
        self.member_ID = member_ID
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.phone = phone
        self.email = email