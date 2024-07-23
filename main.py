import sys
import aspose.words as aw
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog, QTextEdit

class Text_processor(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        uic.loadUi('choose_option.ui', self)

        self.create_btn.clicked.connect(self.createFile)
        self.open_btn.clicked.connect(self.openFile)

    def openFile(self):
        fileName = QFileDialog.getOpenFileName(self, 'OpenFile')[0]
        print(fileName)
        doc = aw.Document(fileName)
        doc.save("Output.html")

        uic.loadUi('edit.ui', self)

        self.page = QTextEdit()
        self.page.setStyleSheet("""background-color: rgb(255, 255, 255);
                                  border-radius: 3px;""")

        with (open('Output.html', 'r', encoding="utf-8") as f):
            html = f.read()

            indx1 = html.find(
                "<div style=\"-aw-headerfooter-type:header-primary; clear:both\"><p style=\"margin-top:0pt;")
            indx2 = (html.find("https://products.aspose.com/words/temporary-license/</span></a></p>")
                     + len("https://products.aspose.com/words/temporary-license/</span></a></p>"))
            html = html.replace(html[indx1:indx2], "")

            indx3 = html.find("<div style=\"-aw-headerfooter-type:footer-primary; clear:both\"><p style=\"margin-top:")
            indx4 = (html.find("2003-2024 Aspose Pty Ltd.</span></p></div>")
                     + len("2003-2024 Aspose Pty Ltd.</span></p></div>"))
            html = html.replace(html[indx3:indx4], "")

            self.page.setHtml(html)

        self.txt_field.addWidget(self.page)

    def createFile(self):
        print()


def main():
    app = QApplication(sys.argv)

    main = Text_processor()
    main.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()