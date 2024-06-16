from Controller.DataEncrypter import DataEncrypter
from Model.Log import Log
import datetime
import ast


class Logger:
    def __init__(self, log_file = 'log.txt', encrypter = DataEncrypter(), service = None):
        self.log_file = log_file
        self.encrypter = encrypter
        self.counter = 0
        self.service = service

    def log(self, message):
        message = self.encrypter.encrypt_data_list(message.__iter__())
        with open(self.log_file, 'a') as f:
            f.write(f'{message}\n')

    def read_date(self):
        logs = []
        with open("last_date.txt", 'r') as f:
            for line in f:
                logs.append(line)
        return logs[0]

    def write_date(self):
        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("last_date.txt", 'w') as f:
            f.write(f'{date}')


    def read(self):
        logs = []
        with open(self.log_file, 'r') as f:
            for line in f:
                logs.append(ast.literal_eval(line))
                self.counter += 1
        return logs

    def create_log(self, username=None, description=None, additional_information=None, suspicious=None, service=None):
        log = Log.create_empty_log()
        collection = service.get_all()
        if self.counter == 0:
            log.set_id(len(collection) + 1)
            self.counter = len(collection) + 2
        else:
            log.set_id(self.counter)
            self.counter += 1
    
        log.set_username(username)
        log.set_description(description)
        log.set_additional_information(additional_information)
        log.set_suspicious("Yes" if suspicious else "No")
        
        service.create(log)
        

    