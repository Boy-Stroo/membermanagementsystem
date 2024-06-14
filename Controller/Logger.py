import DataEncrypter


class Logger:
    def __init__(self, log_file, encrypter: DataEncrypter):
        self.log_file = log_file
        self.encrypter = encrypter

    def log(self, message):
        message = self.encrypter.encrypt(message)
        with open(self.log_file, 'a') as f:
            f.write(message + '\n')

    def read(self):
        logs = []
        with open(self.log_file, 'r') as f:
            for line in f:
                logs.append(self.encrypter.decrypt(line))

        return logs
        

    