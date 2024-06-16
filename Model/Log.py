import datetime

class Log:
    # self.columns = ['id', 'date', 'time', 'Username', 'description', 'additional_information', 'suspicious']

    def __init__(self, id, date, time, username, description, additional_information, suspicious):
        self.id = id
        self.date = date
        self.time = time
        self.username = username
        self.description = description
        self.additional_information = additional_information
        self.suspicious = suspicious

    def create_empty_log():
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        time = datetime.datetime.now().strftime("%H:%M:%S")
        return Log(None, date, time, None, None, None, None)

    def __iter__(self):
        yield self.id
        yield self.date
        yield self.time
        yield self.username
        yield self.description
        yield self.additional_information
        yield self.suspicious

    def set_id(self, id):
        self.id = id
    
    def get_id(self):
        return self.id

    def set_date(self, date):
        self.date = date

    def set_time(self, time):
        self.time = time
    
    def get_time(self):
        return self.time

    def set_username(self, username):
        self.username = username
    
    def set_description(self, description):
        self.description = description
    
    def set_additional_information(self, additional_information):
        self.additional_information = additional_information
    
    def set_suspicious(self, suspicious):
        self.suspicious = suspicious
    
    def __str__(self) -> str:
        return f"{self.id} {self.date} {self.time} {self.username} {self.description} {self.additional_information} {self.suspicious}"