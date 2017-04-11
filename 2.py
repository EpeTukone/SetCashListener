# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QToolTip, QPushButton, QWidget
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import QCoreApplication

class SetCashListener(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a Укажите адрес сервера widget')
        btn.resize(btn.sizeHint())
        btn.move(10, 50)


        qbtn = QPushButton('Quit', self)
        qbtn.setToolTip('Quit')
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(100, 50)


        self.setToolTip('This is a <b>QWidget</b> widget')
        self.setGeometry(300, 300, 300, 220)
        self.setWindowTitle('SetCashListener')
        self.setWindowIcon(QIcon('icon-32x32.ico'))

        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    set10 = SetCashListener()
    sys.exit(app.exec_())

