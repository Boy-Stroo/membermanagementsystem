from Service.Service import Service
from Controller.Logger import Logger

class LogService(Service):
    def __init__(self):
        super().__init__()
        self.table = 'logs'
        self.columns = ['id', 'date', 'time', 'username', 'description', 'additional_information', 'suspicious']
        self.logger = Logger()

    def get_all(self):
        return self.logger.read()

    def create(self, data):
        return self.logger.log(data)