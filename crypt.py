from cryptography.fernet import Fernet


class Crypt:
    def __init__(self, key: str):
        self._key: bytes = key.encode()
        self._f = Fernet(self._key)

    def encrypt(self, value: str) -> bytes:
        encrypted_value = self._f.encrypt(value.encode())
        return encrypted_value

    def decrypt(self, value: bytes) -> str:
        decrypted_value = self._f.decrypt(value)
        return decrypted_value.decode('utf-8')
