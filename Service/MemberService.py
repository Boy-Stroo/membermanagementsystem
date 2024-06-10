from Service.Service import Service


class MemberService(Service):
    def __init__(self):
        super().__init__()
        self.table = 'members'
        self.columns = {
            'id' : 'INTEGER PRIMARY KEY',
            'member_id' : 'TEXT NOT NULL',
            'first_name' : 'TEXT NOT NULL',
            'last_name' : 'TEXT NOT NULL',
            'age' : 'TEXT NOT NULL',
            'gender' : 'TEXT NOT NULL',
            'weight' : 'TEXT NOT NULL',
            'street_name' : 'TEXT NOT NULL',
            'house_number' : 'TEXT NOT NULL',
            'zip_code' : 'TEXT NOT NULL',
            'city' : 'TEXT NOT NULL',
            'email_address' : 'TEXT NOT NULL',
            'mobile_phone' : 'TEXT NOT NULL',
            'registration_date' : 'TEXT NOT NULL'
        }
        
        # ['id', 'name', 'birthdate', 'address', 'phone', 'email']
