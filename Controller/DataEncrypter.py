
from hashlib import pbkdf2_hmac
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os


class DataEncrypter:

    def hashPassword(self, password: str, salt: bytes):
        iterations = 100_000
        return pbkdf2_hmac('sha256', password.encode(), salt, iterations).hex()

    def generate_salt(self):
         return os.urandom(16)
    
    def encrypt_data_list(self, args):
        encrypted_data = []
        key = self.load_public_key()
        for arg in args:
            if type(arg) is not str:
                arg = str(arg) 
            encoded = arg.encode()
            encrypted_data.append(key.encrypt(
                encoded,
                padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None)))
        
        return encrypted_data
    
    def encrypt_data(self, arg : str):
        key = self.load_public_key()
        encoded = arg.encode()
        return key.encrypt(
                encoded,
                padding.OAEP(
                        mgf=padding.MGF1(algorithm=hashes.SHA256()),
                        algorithm=hashes.SHA256(),
                        label=None))
            
    def decrypt_data(self, args):
        decrypted_data = []
        key = self.load_private_key()
        for arg in args:
            decrypted_data.append(key.decrypt(
                            arg,
                            padding.OAEP(
                                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                algorithm=hashes.SHA256(),
                                label=None
                            )).decode())
            
        return decrypted_data


    def load_public_key(self):
        with open('public_key.pem', "rb") as key_file:
            return serialization.load_pem_public_key(key_file.read())
        
    def load_private_key(self):
        with open('private_key.pem', "rb") as key_file:
            return serialization.load_pem_private_key(key_file.read(), password=None)
        
    

        


if (__name__ == "__main__"):
    wachtwoord = ["Boy Stroo", "Welkom12", "Super admin"]
    print(wachtwoord)
    data_encrypter = DataEncrypter()

    encrypted = data_encrypter.encrypt_data_list(wachtwoord)
    print(encrypted)

    decrypted = data_encrypter.decrypt_data(encrypted)

    print(decrypted)
    
