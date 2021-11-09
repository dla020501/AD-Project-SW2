import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *



#메인화면 인터페이스 클래스
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 확인 버튼 생성
        checkButton = QPushButton('확인', self)
        checkButton.clicked.connect(self.checkButton_clicked)

        grid = QGridLayout()

        grid.addWidget(self.choosePersonNumber(), 0, 0)
        grid.addWidget(self.chooseGameBoard(), 0, 1)

        vbox = QVBoxLayout()
        vbox.addLayout(grid)
        vbox.addWidget(checkButton)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 200)
        self.show()

    # 몇인용 게임인지 선택할 수 있는 그룹박스
    def choosePersonNumber(self):
        groupbox = QGroupBox('몇명에서 플레이할 것인지 선택하시오')
        self.aloneButton = QRadioButton('1인용', self)
        self.aloneButton.clicked.connect(self.setGameWidget)

        self.withButton = QRadioButton('2인용', self)
        self.withButton.clicked.connect(self.setGameWidget)

        # 버튼들을 수직으로 정렬
        vbox = QVBoxLayout()
        vbox.addWidget(self.aloneButton)
        vbox.addWidget(self.withButton)
        groupbox.setLayout(vbox)

        return groupbox

    # 게임판의 크기를 고를 수 있는 그룹박스
    def chooseGameBoard(self):
        groupbox = QGroupBox('게임판을 선택하시오')
        self.triGameBoard = QRadioButton('3 X 3', self)
        self.triGameBoard.clicked.connect(self.setGameWidget)

        self.quadGameBoard = QRadioButton('4 X 4', self)
        self.quadGameBoard.clicked.connect(self.setGameWidget)

        self.pentaGameBoard = QRadioButton('5 X 5', self)
        self.pentaGameBoard.clicked.connect(self.setGameWidget)

        # 버튼들을 수직으로 정렬
        vbox = QVBoxLayout()
        vbox.addWidget(self.triGameBoard)
        vbox.addWidget(self.quadGameBoard)
        vbox.addWidget(self.pentaGameBoard)
        groupbox.setLayout(vbox)

        return groupbox

    # 그룹 박스에서 선택한 것들을 가지고 확인 버튼 눌렀을 시 넘어가야 하는 화면의 인덱스 값 정의
    def setGameWidget(self):
        self.widgetCurrentIndex = 0

        if self.aloneButton.isChecked():
            if self.triGameBoard.isChecked():
                self.widgetCurrentIndex = 1 # 1인용이고 3x3일 때
            elif self.quadGameBoard.isChecked():
                self.widgetCurrentIndex = 2 # 1인용이고 4x4일 때
            elif self.pentaGameBoard.isChecked():
                self.widgetCurrentIndex = 3 # 1인용이고 5x5일 때

        elif self.withButton.isChecked():
            if self.triGameBoard.isChecked():
                self.widgetCurrentIndex = 4 # 2인용이고 3x3일 때
            elif self.quadGameBoard.isChecked():
                self.widgetCurrentIndex = 5 # 2인용이고 4x4일 때
            elif self.pentaGameBoard.isChecked():
                self.widgetCurrentIndex = 6 # 2인용이고 5x5일 때

    # setGameWidget을 통해 정해진 인덱스에 맞는 화면으로 전환
    def checkButton_clicked(self):
        widget.setCurrentIndex(self.widgetCurrentIndex)

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        button = QPushButton('뒤로', self)
        button.clicked.connect(self.backButton_clicked)

        self.show()

    def backButton_clicked(self):
        widget.setCurrentIndex(0)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 화면 전환용 widget 생성
    widget = QtWidgets.QStackedWidget()

    # 레이아웃 인스턴스 생성
    mainWindow = MainWindow()
    secondWindow = SecondWindow()

    widget.addWidget(mainWindow) # 인덱스 0
    widget.addWidget(secondWindow) # 인덱스 1

    widget.show()

    sys.exit(app.exec_())