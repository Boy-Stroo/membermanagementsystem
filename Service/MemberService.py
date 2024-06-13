from Service.Service import Service


class MemberService(Service):
    def __init__(self):
        super().__init__()
        self.table = 'members'
        self.columns = ['id', 'name', 'birthdate', 'address', 'phone', 'email', 'registration_date']
