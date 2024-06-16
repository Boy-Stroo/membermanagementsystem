from zipfile import ZipFile
from datetime import datetime
import zipfile
import os
import glob

class BackupManager:
    def __init__(self, *args):
        self.to_backup = args

    def backupData(self):
        # backup database.db and save it to a zip
        files_to_backup = ['database.db', 'log.txt', 'last_date.txt']

        # unique filename
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_filename = f'backup_{timestamp}.zip'

        with zipfile.ZipFile(backup_filename, 'w') as backup_zip:
            for file in files_to_backup:
                if os.path.exists(file):
                    backup_zip.write(file)
                else:
                    print(f'Warning: {file} does not exist and will not be included in the backup.')

        print(f'Backup created successfully: {backup_filename}')
        input("Press Enter to continue...")

    def restoreData(self):
        # Find the latest backup file based on the timestamp in the filename
        list_of_files = glob.glob('backup_*.zip')
        if not list_of_files:
            print("No backup file found.")
            return
        
        latest_backup = max(list_of_files, key=os.path.getctime)
        
        # Define the files to restore
        files_to_restore = ['database.db', 'log.txt', 'last_date.txt']

        # Restore the files from the latest backup zip
        with zipfile.ZipFile(latest_backup, 'r') as backup_zip:
            for file in files_to_restore:
                if file in backup_zip.namelist():
                    backup_zip.extract(file, path='.')
                    print(f"Restored {file} from {latest_backup}")
                else:
                    print(f"{file} not found in the backup {latest_backup}")

        print("Data restoration completed.")
        input("Press Enter to continue...")