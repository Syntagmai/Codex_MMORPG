
import hashlib
import secrets
import base64
from cryptography.fernet import Fernet

class SecurityManager:
    """Gerenciador de segurança com criptografia"""
    
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
    
    def hash_password(self, password):
        """Cria hash seguro de senha"""
        salt = secrets.token_hex(16)
        hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
        return salt + hash_obj.hex()
    
    def verify_password(self, password, stored_hash):
        """Verifica senha contra hash armazenado"""
        salt = stored_hash[:32]
        hash_obj = hashlib.pbkdf2_hmac('sha256', password.encode(), salt.encode(), 100000)
        return stored_hash[32:] == hash_obj.hex()
    
    def encrypt_data(self, data):
        """Criptografa dados"""
        return self.cipher_suite.encrypt(data.encode())
    
    def decrypt_data(self, encrypted_data):
        """Descriptografa dados"""
        return self.cipher_suite.decrypt(encrypted_data).decode()
    
    def generate_secure_token(self, length=32):
        """Gera token seguro"""
        return secrets.token_urlsafe(length)

# Instância global
security_manager = SecurityManager()
