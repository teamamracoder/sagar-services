import hashlib

class EncryptionUtils:
     
    @staticmethod
    def encrypt(password):
        # Using MD5 hashing for encryption
        hashed_password = hashlib.md5(password.encode()).hexdigest()
        return hashed_password