import sys

from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QMessageBox, QLabel


#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5 import uic



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.resize(250, 150)
        self.move(300, 300)
        self.setWindowTitle('Simple')

        self.le = QLineEdit(self)
        self.le.move(22, 22)
        self.le.returnPressed.connect(self.pressedKeys)

        self.lbl = QLabel(self)
        self.lbl.move(22, 50)
        self.lbl.resize(100, 20)

        self.show()

    def pressedKeys(self):
        print(self.le.text())
        self.lbl.setText(self.le.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())