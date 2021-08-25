from cryptography.fernet import Fernet
import base64


class Crypt:
    def __init__(self, key: bytes):
        self._key: bytes = self._convert_key(key)
        self._f = Fernet(self._key)

    @staticmethod
    def _convert_key(key: bytes) -> bytes:
        return base64.urlsafe_b64encode(key[:32])

    def encrypt(self, value: str) -> str:
        encrypted_value = self._f.encrypt(value.encode())
        return encrypted_value.decode('utf-8')

    def decrypt(self, value: str) -> str:
        decrypted_value = self._f.decrypt(value.encode())
        return decrypted_value.decode('utf-8')
