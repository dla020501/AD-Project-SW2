import random
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont

class Game(QMainWindow):
    # num은 게임판 크기, ai는 AI의 여부
    def __init__(self, num, ai):
        super().__init__()
        self.index = num
        self.mark = "O"
        self.setWindowTitle("틱택토")

        self.menu = self.menuBar()
        self.menu.addAction("시작", self.start)
        self.menu.addAction("초기화", self.reset)


        self.statusBar().showMessage("게임을 시작하려면 시작 버튼을 눌러주세요.")

        self.grid = QGridLayout()
        self.grid.setSpacing(1)
        self.fnt = QFont()
        self.fnt.setBold(True)
        self.fnt.setPixelSize(50)

        self.arr = []
        self.win = []
        self.sw = 0 #게임의 시작상태 저장, 비활성화 라는 뜻

        for r in range(self.index):
            self.arr.append([])
            self.win.append([])
            for c in range(self.index):
                self.arr[r].append(QPushButton(""))
                self.win[r].append("")
                self.arr[r][c].setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
                self.arr[r][c].setObjectName(str(r)+str(c))
                self.arr[r][c].setFont(self.fnt)
                self.grid.addWidget(self.arr[r][c], r, c)


            w = QWidget()
            w.setLayout(self.grid)
            self.setCentralWidget(w)
            self.setGeometry(2800, 500, 300, 300)

            self.show()

        # 각각의 버튼마다 클릭했을 시 연결되는 함수 선언
        self.SetButtonConnected(self.index, ai)

    def start(self):
        self.sw = 1
        self.reset()


    def reset(self):
        if self.sw == 1:
            for r in range(self.index):
                for c in range(self.index):
                    self.arr[r][c].setText("")
            self.mark = "O"

    def SetButtonConnected(self, num, ai):
        if num == 3:
            self.arr[0][0].clicked.connect(lambda: self.chk(0, 0, ai))
            self.arr[0][1].clicked.connect(lambda: self.chk(0, 1, ai))
            self.arr[0][2].clicked.connect(lambda: self.chk(0, 2, ai))
            self.arr[1][0].clicked.connect(lambda: self.chk(1, 0, ai))
            self.arr[1][1].clicked.connect(lambda: self.chk(1, 1, ai))
            self.arr[1][2].clicked.connect(lambda: self.chk(1, 2, ai))
            self.arr[2][0].clicked.connect(lambda: self.chk(2, 0, ai))
            self.arr[2][1].clicked.connect(lambda: self.chk(2, 1, ai))
            self.arr[2][2].clicked.connect(lambda: self.chk(2, 2, ai))
        elif num == 4:
            self.arr[0][0].clicked.connect(lambda: self.chk(0, 0, ai))
            self.arr[0][1].clicked.connect(lambda: self.chk(0, 1, ai))
            self.arr[0][2].clicked.connect(lambda: self.chk(0, 2, ai))
            self.arr[0][3].clicked.connect(lambda: self.chk(0, 3, ai))
            self.arr[1][0].clicked.connect(lambda: self.chk(1, 0, ai))
            self.arr[1][1].clicked.connect(lambda: self.chk(1, 1, ai))
            self.arr[1][2].clicked.connect(lambda: self.chk(1, 2, ai))
            self.arr[1][3].clicked.connect(lambda: self.chk(1, 3, ai))
            self.arr[2][0].clicked.connect(lambda: self.chk(2, 0, ai))
            self.arr[2][1].clicked.connect(lambda: self.chk(2, 1, ai))
            self.arr[2][2].clicked.connect(lambda: self.chk(2, 2, ai))
            self.arr[2][3].clicked.connect(lambda: self.chk(2, 3, ai))
            self.arr[3][0].clicked.connect(lambda: self.chk(3, 0, ai))
            self.arr[3][1].clicked.connect(lambda: self.chk(3, 1, ai))
            self.arr[3][2].clicked.connect(lambda: self.chk(3, 2, ai))
            self.arr[3][3].clicked.connect(lambda: self.chk(3, 3, ai))
        else:
            self.arr[0][0].clicked.connect(lambda: self.chk(0, 0, ai))
            self.arr[0][1].clicked.connect(lambda: self.chk(0, 1, ai))
            self.arr[0][2].clicked.connect(lambda: self.chk(0, 2, ai))
            self.arr[0][3].clicked.connect(lambda: self.chk(0, 3, ai))
            self.arr[0][4].clicked.connect(lambda: self.chk(0, 4, ai))
            self.arr[1][0].clicked.connect(lambda: self.chk(1, 0, ai))
            self.arr[1][1].clicked.connect(lambda: self.chk(1, 1, ai))
            self.arr[1][2].clicked.connect(lambda: self.chk(1, 2, ai))
            self.arr[1][3].clicked.connect(lambda: self.chk(1, 3, ai))
            self.arr[1][4].clicked.connect(lambda: self.chk(1, 4, ai))
            self.arr[2][0].clicked.connect(lambda: self.chk(2, 0, ai))
            self.arr[2][1].clicked.connect(lambda: self.chk(2, 1, ai))
            self.arr[2][2].clicked.connect(lambda: self.chk(2, 2, ai))
            self.arr[2][3].clicked.connect(lambda: self.chk(2, 3, ai))
            self.arr[2][4].clicked.connect(lambda: self.chk(2, 4, ai))
            self.arr[3][0].clicked.connect(lambda: self.chk(3, 0, ai))
            self.arr[3][1].clicked.connect(lambda: self.chk(3, 1, ai))
            self.arr[3][2].clicked.connect(lambda: self.chk(3, 2, ai))
            self.arr[3][3].clicked.connect(lambda: self.chk(3, 3, ai))
            self.arr[3][4].clicked.connect(lambda: self.chk(3, 4, ai))
            self.arr[4][0].clicked.connect(lambda: self.chk(4, 0, ai))
            self.arr[4][1].clicked.connect(lambda: self.chk(4, 1, ai))
            self.arr[4][2].clicked.connect(lambda: self.chk(4, 2, ai))
            self.arr[4][3].clicked.connect(lambda: self.chk(4, 3, ai))
            self.arr[4][4].clicked.connect(lambda: self.chk(4, 4, ai))

    # row는 행, column은 열, ai는 AI 함수 실행 트리거
    def chk(self, row, column, ai):
        if self.sw == 1:
            if self.arr[row][column].text() != "":
                return
            else:
                self.arr[row][column].setText(self.mark)
                for r in range(self.index):
                    for c in range(self.index):
                        self.win[r][c] = self.arr[r][c].text()

                # 게임판의 크기에 맞추어 게임의 승패 여부 가리는 함수 실행
                if self.Checking():
                    self.sw = 0

                if self.mark == "O":
                    self.mark = "X"
                else:
                    self.mark = "O"

            # ai가 True일 때 실행
            if ai:
                self.AI()

    # AI 구현한 함수
    # 내가 이기거나 상대방이 이기는 경우가 없을때는 랜덤으로 배치하도록 설계
    def AI(self):
        if self.sw == 1:
            array = [["" for cal in range(self.index)] for raw in range(self.index)]
            emptyIndex = []
            self.breakSwitch = 0

            for r in range(self.index):
                for c in range(self.index):
                    array[r][c] = self.win[r][c]
                    if self.win[r][c] == "":
                        emptyIndex.append([r, c])

            for index in emptyIndex:
                a = index[0]
                b = index[1]

                self.AICheckingMark(array, a, b)
                self.AIDefenseMark(array, a, b)

                if self.breakSwitch == 1:
                    break

            if self.breakSwitch == 0:
                i = random.randrange(0, len(emptyIndex))
                self.chk(emptyIndex[i][0], emptyIndex[i][1], False)

    # 게임 승패 여부 가리는 함수
    def Checking(self):
        for i in range(self.index):
            rawsum = self.win[i][0]
            colsum = self.win[0][i]
            updiag = self.win[0][0]
            downdiag = self.win[0][self.index - 1]
            for j in range(1, self.index):
                rawsum += self.win[i][j]
                colsum += self.win[j][i]
                updiag += self.win[j][j]
                downdiag += self.win[j][self.index - (1 + j)]

            if self.mark * self.index == rawsum or self.mark * self.index == colsum or \
                    self.mark * self.index == updiag or self.mark * self.index == downdiag:
                QMessageBox.about(self, "종료", self.mark + "가 이겼습니다!")
                return True

        count = 0
        for r in range(self.index):
            for c in range(self.index):
                if self.arr[r][c].text() != '':
                    count += 1

        if count == self.index * self.index:
            QMessageBox.about(self, "종료", "비겼습니다!")
            return True

        return False

    # AI 본인이 이길 수 있는지 확인하고 그 자리에 놓을 수 있는 알고리즘
    def AICheckingMark(self, array, a, b):
        array[a][b] = self.mark
        for i in range(self.index):
            rawsum = array[a][b] if a == i and b == 0 else array[i][0]
            colsum = array[a][b] if a == 0 and b == i else array[0][i]
            updiag = array[a][b] if a == 0 and b == 0 else array[0][0]
            downdiag = array[a][b] if a == 0 and b == self.index - 1 else array[0][self.index - 1]
            for j in range(1, self.index):
                rawsum += array[a][b] if a == i and b == j else array[i][j]
                colsum += array[a][b] if a == j and b == i else array[j][i]
                updiag += array[a][b] if a == j and b == j else array[j][j]
                downdiag += array[a][b] if a == j and b == self.index - (1 + j) else array[j][self.index - (1 + j)]

            if self.mark * self.index == rawsum or self.mark * self.index == colsum or \
                    self.mark * self.index == updiag or self.mark * self.index == downdiag:
                self.chk(a, b, False)
                self.breakSwitch = 1
                break


    # 상대가 이긴다면 막는 알고리즘
    def AIDefenseMark(self, array, a, b):
        for i in range(self.index):
            rawsum = "O" if a == i and b == 0 else array[i][0]
            colsum = "O" if a == 0 and b == i else array[0][i]
            updiag = "O" if a == 0 and b == 0 else array[0][0]
            downdiag = "O" if a == 0 and b == self.index - 1 else array[0][self.index - 1]
            for j in range(1, self.index):
                rawsum += "O" if a == i and b == j else array[i][j]
                colsum += "O" if a == j and b == i else array[j][i]
                updiag += "O" if a == j and b == j else array[j][j]
                downdiag += "O" if a == j and b == self.index - (1 + j) else array[j][self.index - (1 + j)]

            if "O" * self.index == rawsum or "O" * self.index == colsum or \
                    "O" * self.index == updiag or "O" * self.index == downdiag:
                self.chk(a, b, False)
                self.breakSwitch = 1
                break