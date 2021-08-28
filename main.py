import sys

from PyQt6 import QtWidgets as QW
from ui import ui


def main():
    app = QW.QApplication(sys.argv)
    window = ui.LoginWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()