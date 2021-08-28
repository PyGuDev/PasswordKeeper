
class Account:
    def __init__(self, data: list):
        self._id = data[0]
        self._login = data[1]
        self._salt = data[2]
        self._key = data[3]

    @property
    def id(self) -> int:
        return self._id

    @property
    def login(self) -> str:
        return self._login

    @property
    def salt(self) -> str:
        return self._salt

    @property
    def key(self) -> str:
        return self._key
