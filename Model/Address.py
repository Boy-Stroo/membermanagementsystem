import random

class Address:

    cities = ['Amsterdam', 'Rotterdam', 'Den Haag', 'Utrecht', 'Eindhoven', 'Tilburg', 'Groningen', 'Almere', 'Breda', 'Nijmegen']

    def __init__(self, street_name : str, house_number : int, city : str, zipcode : str):
        self.street_name = street_name
        self.house_number = house_number
        self.zipcode = zipcode
        self.city = random.choice(self.cities)



    def __str__(self):
        return f'{self.street_name} {self.house_number}, {self.zipcode} {self.city}'

    def set_street_name(self, street_name):
        self.street_name = street_name

    def set_house_number(self, house_number):
        self.house_number = house_number
    
    def set_zipcode(self, zipcode):
        self.zipcode = zipcode
