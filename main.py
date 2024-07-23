import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic


class Text_processor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        uic.loadUi('choose_option.ui', self)

        self.create_btn.clicked.connect(self.createFile)
        self.open_btn.clicked.connect(self.openFile)

    def openFile(self):
        print()

    def createFile(self):
        print()


def main():
    app = QApplication(sys.argv)

    main = Text_processor()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()