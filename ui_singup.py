# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'singup.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthForm(object):
    def setupUi(self, AuthForm):
        AuthForm.setObjectName("AuthForm")
        AuthForm.resize(500, 400)
        AuthForm.setMinimumSize(QtCore.QSize(500, 400))
        AuthForm.setMaximumSize(QtCore.QSize(500, 400))
        AuthForm.setAutoFillBackground(False)
        AuthForm.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0#3c1053, stop:1 #ad5389);")
        self.layoutWidget = QtWidgets.QWidget(AuthForm)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 501, 405))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(20, 60, 20, 60)
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName("verticalLayout")
        self.title_label = QtWidgets.QLabel(self.layoutWidget)
        self.title_label.setStyleSheet("color: white;\n"
"font-size: 30px;\n"
"background: rgba(255,255,255, 0);")
        self.title_label.setAlignment(QtCore.Qt.AlignCenter)
        self.title_label.setObjectName("title_label")
        self.verticalLayout.addWidget(self.title_label)
        self.input_login = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.input_login.setFont(font)
        self.input_login.setStyleSheet("background: rgba(255, 255, 255, 0.5);\n"
"height: 29px;\n"
"border-radius: 10px;\n"
"border: 0;\n"
"padding: 10px;\n"
"color: white;\n"
"font-size: 24px;")
        self.input_login.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.input_login.setObjectName("input_login")
        self.verticalLayout.addWidget(self.input_login)
        self.input_password = QtWidgets.QLineEdit(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.input_password.setFont(font)
        self.input_password.setStyleSheet("background: rgba(255, 255, 255, 0.5);\n"
"height: 29px;\n"
"border-radius: 10px;\n"
"border: 0;\n"
"padding: 10px;\n"
"color: white;\n"
"font-size: 24px;")
        self.input_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.input_password.setObjectName("input_password")
        self.verticalLayout.addWidget(self.input_password)
        self.singup_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.singup_btn.setStyleSheet("border: 0;\n"
"border-radius: 10px;\n"
"font-size: 24px;\n"
"padding: 10px;\n"
"background: rgb(12, 189, 18);\n"
"color: white;\n"
"")
        self.singup_btn.setObjectName("singup_btn")
        self.verticalLayout.addWidget(self.singup_btn)
        self.login_btn = QtWidgets.QPushButton(self.layoutWidget)
        self.login_btn.setStyleSheet("border: 0;\n"
"border-radius: 10px;\n"
"font-size: 24px;\n"
"padding: 10px;\n"
"background: #179bf3;\n"
"color: white;\n"
"")
        self.login_btn.setObjectName("login_btn")
        self.verticalLayout.addWidget(self.login_btn)
        self.error_label = QtWidgets.QLineEdit(self.layoutWidget)
        self.error_label.setStyleSheet("color: red;\n"
"border: 0;\n"
"background: rgba(255,255,255, 0%)")
        self.error_label.setObjectName("error_label")
        self.verticalLayout.addWidget(self.error_label)

        self.retranslateUi(AuthForm)
        QtCore.QMetaObject.connectSlotsByName(AuthForm)

    def retranslateUi(self, AuthForm):
        _translate = QtCore.QCoreApplication.translate
        AuthForm.setWindowTitle(_translate("AuthForm", "Регистрация"))
        self.title_label.setText(_translate("AuthForm", "Регистрация"))
        self.input_login.setPlaceholderText(_translate("AuthForm", "Login"))
        self.input_password.setPlaceholderText(_translate("AuthForm", "Password"))
        self.singup_btn.setText(_translate("AuthForm", "Регистрация"))
        self.login_btn.setText(_translate("AuthForm", "Войти"))
