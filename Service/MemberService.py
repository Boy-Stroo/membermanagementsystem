from Service.Service import Service


class MemberService(Service):
    def __init__(self):
        super().__init__()
        self.table = 'members'
        self.columns = ['id', 'first_name', 'last_name', 'age', 'gender', 'weight', 'address',  'email', 'telephone_number', 'registration_date']
