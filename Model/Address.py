class Address:
    def __init__(self, street_name : str, house_number : int, city : str, zipcode : str):
        self.street_name = street_name
        self.house_number = house_number
        self.zipcode = zipcode
        self.city = city

    def __str__(self):
        return f'{self.street_name} {self.house_number} {self.zipcode} {self.city}'