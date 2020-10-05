import sqlite3
import hashlib
import os


class ControllerDb:
    def __init__(self):
        self.USER_ID = -1
        db = sqlite3.connect('data.db')
        sql = db.cursor()

        sql.execute("""CREATE TABLE IF NOT EXISTS account(
                id INTEGER PRIMARY KEY,
                login VARCHAR(30) UNIQUE,
                salt TEXT,
                key TEXT)
            """)
        db.commit()
        sql.execute("""CREATE TABLE IF NOT EXISTS service(
                id INTEGER PRIMARY KEY,
                account_id INTEGER REFERENCES account(id),
                name TEXT,
                email VARCHAR(30),
                password TEXT)
            """)
        db.commit()
        db.close()

    def register(self, login, password):
        salt = os.urandom(32)
        key = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode('utf-8'),
            salt,
            10000
        )

        db = sqlite3.connect('data.db')
        sql = db.cursor()
        try:
            sql.execute("INSERT INTO account(login, salt, key) VALUES('{}', '{}', '{}')".format(login, salt.hex(), key.hex()))
        except:
            return False
        db.commit()
        db.close()
        return True

    def authorization(self, login, password):
        db = sqlite3.connect('data.db')
        sql = db.cursor()
        sql.execute("SELECT * FROM account")
        accounts_list = sql.fetchall()
        db.close()
        for account in accounts_list:
            if login == account[1]:

                key = hashlib.pbkdf2_hmac(
                    'sha256',
                    password.encode('utf-8'),
                    bytes.fromhex(account[2]),
                    10000
                )
                if key.hex() == account[3]:
                    self.USER_ID = account[0]
                    return self.USER_ID

    def add_service(self, user_id, name_service, email, password):
        db = sqlite3.connect('data.db')
        sql = db.cursor()
        sql.execute("INSERT INTO service(account_id, name, email, password) VALUES({}, '{}', '{}', '{}')".format(user_id, name_service, email, password))
        db.commit()
        db.close()

    def show_service(self, user_id):
        db = sqlite3.connect('data.db')
        sql = db.cursor()
        sql.execute("SELECT sv.id, sv.name, sv.email, sv.password FROM service sv WHERE sv.account_id={}".format(user_id))
        result = sql.fetchall()
        db.close()
        return result

    def update_service(self, id, service_name, email, password):
        db = sqlite3.connect('data.db')
        sql = db.cursor()
        sql.execute("UPDATE service SET name='{}', email='{}', password='{}' WHERE id={}".format(service_name, email, password, id))
        db.execute()

    def del_service(self, id_service):
        db = sqlite3.connect('data.db')
        sql = db.cursor()
        sql.execute("DELETE FROM service WHERE id={}".format(id_service))
        db.commit()
        db.close()
