from PyQt5 import QtWidgets as QW
from ui import SingUpWindow, LoginWindow, MainWindow
import sys


def main():
    app = QW.QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()