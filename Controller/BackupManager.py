from zipfile import ZipFile

class BackupManager:
    def __init__(self, *args):
        self.to_backup = args

    def backupData(self):
        # backup database.db and save it to a zip
        with ZipFile('backup.zip', 'w') as backup:
            for arg in self.to_backup:
                backup.write(arg)

    def restoreData(self):
        # restore database.db from backup.zip
        with ZipFile('backup.zip', 'r') as backup:
            backup.extract('database.db')

        