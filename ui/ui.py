from PyQt6 import QtWidgets as QW, QtGui

from . import ui_login
from . import ui_main
from . import ui_signup
from controller import ControllerDb

FormSingUp = ui_signup.Ui_AuthForm
FormSingIn = ui_login.Ui_AuthForm
FormMain = ui_main.Ui_MainWindow


class MainWindow(QW.QMainWindow, FormMain):
    def __init__(self, parent=None, user_id=-1):
        QW.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        ico = QtGui.QIcon('favicon.png')
        self.setWindowIcon(ico)
        self.user_id = user_id
        self.controller = ControllerDb()
        self.show_service()
        self.add_btn.clicked.connect(self.add_service)
        self.del_btn.clicked.connect(self.del_service)

    def show_service(self):
        result = self.controller.show_service(self.user_id)
        if result == []:
            return 0
        self.list_service.setRowCount(len(result))
        self.list_service.setColumnCount(len(result[0]))
        row, column = 0, 0
        for items in result:
            for item in items:
                self.list_service.setItem(row, column, QW.QTableWidgetItem(str(item) if type(item)== int else item))
                column += 1
            row += 1
            column = 0

    def add_service(self):
        if self.name_service.text() == '' or self.email_service.text() == '' or self.passw_service.text() == '':
            msgBox = QW.QMessageBox()
            msgBox.setIcon(QW.QMessageBox.Icon.Information)
            msgBox.setText("Предупреждение")
            msgBox.setInformativeText("Заполните все поля")
            msgBox.setStandardButtons(QW.QMessageBox.StandardButton.Ok)
            msgBox.exec()
        else:
            self.controller.add_service(self.user_id, self.name_service.text(), self.email_service.text(), self.passw_service.text())
            self.show_service()

    def del_service(self):
        for item in self.list_service.selectedItems():
            id = int(self.list_service.item(item.row(), 0).text())
            self.controller.del_service(id)
            self.list_service.removeRow(item.row())




class LoginWindow(QW.QWidget, FormSingIn):
    def __init__(self, parent=None):
        QW.QWidget.__init__(self, parent)
        self.setupUi(self)
        ico = QtGui.QIcon('favicon.png')
        self.setWindowIcon(ico)
        self.setContentsMargins(10, 10, 10, 10)
        self.login_btn.clicked.connect(self.login)
        self.singup_btn.clicked.connect(self.open_singup)
        self.controller = ControllerDb()

    def login(self):
        if self.input_password.text() == '' and self.input_login.text() == '':
            self.error_label.setText("Заполните все поля.")
        if self.check_for_russian(self.input_password.text()):
            self.error_label.setText("Пароль не должен содеражать кирилицу.")
        elif self.check_for_russian(self.input_login.text()):
            self.error_label.setText("Логин не должен содеражать кирилицу.")
        else:
            id = self.controller.authorization(self.input_login.text(), self.input_password.text())
            if type(id) == int:
                self.open_main(id)
            else:
                self.error_label.setText("Неверный логин или пароль")

    def open_singup(self):
        self.singup_screen = SingUpWindow()
        self.singup_screen.show()
        self.close()

    def open_main(self, id):
        self.main_screen = MainWindow(user_id=id)
        self.main_screen.show()
        self.close()

    def check_for_russian(self, string):
        alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
                    "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
        for one_char in string:
            if one_char in alphabet:
                return True
        return False


class SingUpWindow(QW.QWidget, FormSingUp):
    def __init__(self, parent=None):
        QW.QWidget.__init__(self, parent)
        self.setupUi(self)
        ico = QtGui.QIcon('favicon.png')
        self.setWindowIcon(ico)
        self.setContentsMargins(10, 10, 10, 10)
        self.singup_btn.clicked.connect(self.sing_up)
        self.login_btn.clicked.connect(self.open_login)
        self.controller = ControllerDb()

    def sing_up(self):
        if self.input_password.text() == '' and self.input_login.text() == '':
            self.error_label.setText("Заполните все поля.")
            return 0
        if self.check_for_russian(self.input_password.text()):
            self.error_label.setText("Пароль не должен содеражать кирилицу.")
        elif self.check_for_russian(self.input_login.text()):
            self.error_label.setText("Логин не должен содеражать кирилицу.")
        else:
            if self.controller.register(self.input_login.text(), self.input_password.text()):
                self.open_login()
            else:
                self.error_label.setText("Такой ползователь уже существует")

    def open_login(self):
        self.login_screen = LoginWindow()
        self.login_screen.show()
        self.close()

    def check_for_russian(self, string):
        alphabet = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т",
                    "у", "ф", "х", "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
        for one_char in string:
            if one_char in alphabet:
                return True
        return False
