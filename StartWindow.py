import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,QGridLayout,
    QComboBox, QLayout)

from PyQt5.QtGui import QFont
from GameUI import Game

class StartWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initialSetting = [{'3x3': 1, '4x4': 2, '5x5': 3},{'3x3': 4, '4x4': 5, '5x5': 6}]

        start_sentence1 = QLabel("Let's play tic tac toe !", self)
        start_sentence1.setFont(QFont("궁서", 20))
        start_sentence1.setStyleSheet("Color : blue")
        self.howMany = QComboBox(self)
        self.howMany.addItem("혼자하기")
        self.howMany.addItem("둘이하기")

        self.nxn = QComboBox(self)
        self.nxn.addItem("3x3")
        self.nxn.addItem("4x4")
        self.nxn.addItem("5x5")

        self.startButton = QPushButton("START")
        self.startButton.clicked.connect(self.setWindow)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.howMany)
        hbox2.addWidget(self.nxn)
        vbox = QVBoxLayout()
        vbox.addWidget(start_sentence1)
        vbox.addLayout(hbox2)
        vbox.addWidget(self.startButton)

        hbox = QHBoxLayout()
        hbox.addStretch(5)
        hbox.addLayout(vbox)
        hbox.addStretch(1)

        self.setLayout(hbox)
        self.setFixedSize(500,300)
        self.setWindowTitle("Tic Tac Toe")
        self.show()

        mainLayout = QGridLayout()

    def setWindow(self):
        if self.howMany.currentText() == '혼자하기':
            mainSettingdic = self.initialSetting[1]
        else :
            mainSettingdic = self.initialSetting[0]
        widget.setCurrentIndex(mainSettingdic[self.nxn.currentText()])

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 화면 전환용 widget 생성
    widget = QtWidgets.QStackedWidget()
    for i in range(7):
        if i == 0:
            window = StartWindow()
        elif i < 4:
            window = Game(i+2, False)
        # i = 4, 5, 6
        else :
            window = Game(i-1, True)
        widget.addWidget(window)

    widget.show()

    sys.exit(app.exec_())