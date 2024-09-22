from Controller.CollectionController import CollectionController
from Controller.DataEncrypter import DataEncrypter
from Controller.BackupManager import BackupManager
from Model.Log import Log
import datetime

class LogController(CollectionController):

    _instance = None

    def __init__(self, service, input_validator):
        if (LogController._instance != None):
            return LogController._instance

        self.input_validator = input_validator
        self.service = service
        self.data_encrypter = DataEncrypter()
        self.backup_manager = BackupManager()
        self.counter = 0
        
        super().__init__(service, input_validator)
        self._instance = self
        self.reset_collection()

    def get_suspicious_logs(self, date):
        suspicious_logs = []
        date = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        for log in self.collection:
            new_date = datetime.datetime.strptime(f"{log.date} {log.time}" , "%Y-%m-%d %H:%M:%S")
            if new_date > date and log.suspicious == "Yes":
                suspicious_logs.append(log)

        return suspicious_logs

    def reset_collection(self):
        super().reset_collection()

        self.collection = [Log(*log) for log in self.collection]
        self.collection.sort(key=lambda x: x.time)
    
    def backup_system(self):
        self.backup_manager.backupData()
    
    def restore_system(self):
        self.backup_manager.restoreData()