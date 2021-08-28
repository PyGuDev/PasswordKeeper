import sqlite3
import hashlib
import os

from crypt import Crypt
from sqlite3 import Cursor, Connection
from typing import Optional, Tuple


class ControllerDb:
    _USER_ID: int = -1

    def __init__(self):
        self._db_name: str = 'data.db'
        self._create_first_model()
        self._crypt: Optional[Crypt] = None

    def _create_first_model(self):
        db_connect = sqlite3.connect(self._db_name)
        _cursor = db_connect.cursor()
        self._create_model_account(_cursor, db_connect)
        self._create_model_service(_cursor, db_connect)
        db_connect.close()

    def _init_crypt(self, key: bytes):
        self._crypt = Crypt(key)

    @staticmethod
    def _create_model_account(cursor: Cursor, db_connect: Connection):
        cursor.execute("""CREATE TABLE IF NOT EXISTS account(
                       id INTEGER PRIMARY KEY,
                       login VARCHAR(30) UNIQUE,
                       salt TEXT,
                       key TEXT)
                   """)
        db_connect.commit()

    @staticmethod
    def _create_model_service(cursor: Cursor, db_connect: Connection):
        cursor.execute("""CREATE TABLE IF NOT EXISTS service(
                        id INTEGER PRIMARY KEY,
                        account_id INTEGER REFERENCES account(id),
                        name TEXT,
                        email VARCHAR(30),
                        password TEXT)
                    """)
        db_connect.commit()

    @staticmethod
    def _hashing(value: str, salt: str = None) -> Tuple[bytes, bytes]:
        if not salt:
            b_salt = os.urandom(32)
        else:
            b_salt: bytes = bytes.fromhex(salt)
        b_value: bytes = value.encode('utf-8')
        key = hashlib.pbkdf2_hmac(
            'sha256',
            b_value,
            b_salt,
            10000
        )
        return b_salt, key

    def register(self, login: str, password: str) -> bool:
        salt, key = self._hashing(password)
        db = sqlite3.connect(self._db_name)
        cursor = db.cursor()
        try:
            cursor.execute("INSERT INTO account(login, salt, key) VALUES('{}', '{}', '{}')".format(
                login, salt.hex(), key.hex()))
        except:
            return False
        db.commit()
        db.close()
        return True

    def authorization(self, login: str, password: str) -> Optional[int]:
        db = sqlite3.connect(self._db_name)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM account")
        accounts_list = cursor.fetchall()
        db.close()
        for account in accounts_list:
            if login == account[1]:
                _, key = self._hashing(password, account[2])
                if key.hex() == account[3]:
                    self._USER_ID = account[0]
                    self._init_crypt(key)
                    return self._USER_ID

    def add_service(self, user_id: int, name_service: str, email: str, password: str):
        db = sqlite3.connect(self._db_name)
        cursor = db.cursor()
        cursor.execute("INSERT INTO service(account_id, name, email, password) VALUES({}, '{}', '{}', '{}')".format(
            user_id, name_service, email, password))
        db.commit()
        db.close()

    def show_service(self, user_id: int) -> list:
        db = sqlite3.connect(self._db_name)
        cursor = db.cursor()
        cursor.execute("SELECT sv.id, sv.name, sv.email, sv.password FROM service sv WHERE sv.account_id={}".format(
            user_id))
        result = cursor.fetchall()
        db.close()
        return result

    def update_service(self, service_id: int, service_name: str, email: str, password: str):
        db = sqlite3.connect(self._db_name)
        cursor = db.cursor()
        cursor.execute("UPDATE service SET name='{}', email='{}', password='{}' WHERE id={}".format(
            service_name, email, password, service_id))
        db.execute()
        db.close()

    def del_service(self, service_id: int):
        db = sqlite3.connect(self._db_name)
        cursor = db.cursor()
        cursor.execute("DELETE FROM service WHERE id={}".format(service_id))
        db.commit()
        db.close()
