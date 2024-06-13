import bcrypt
import rsa
import os
from helper import FileHelper


class Encrypter:

    def __init__(self):
        self.salt = bcrypt.gensalt()
        self.public_key_path = 'public.txt'
        self.private_key_path = 'private.txt'
        self.private_key = None
        self.public_key = None

    def hash_password(self, password):
        return bcrypt.hashpw(password.encode('utf-8'), self.salt)
    
    def encrypt(self, text):
        pass

    def decrypt(self, text):
        pass

    def get_public_key(self):
        if self.public_key is None:
            if os.path.exists(self.public_key_path):
                self.public_key = FileHelper.read_file(self.public_key_path)
            else:
                self.generate_keys()
        return self.public_key
    
    def get_private_key(self):
        if self.private_key is None:
            if os.path.exists(self.private_key_path):
                self.private_key = FileHelper.read_file(self.private_key_path)
            else:
                self.generate_keys()
        return self.private_key
    
    def generate_keys(self):
        (pubkey, privkey) = rsa.newkeys(512)
        self.public_key = pubkey.load_pkcs1
        self.private_key = privkey.decode('utf-8')
        FileHelper.write_file(self.public_key_path, self.public_key)
        FileHelper.write_file(self.private_key_path, self.private_key)