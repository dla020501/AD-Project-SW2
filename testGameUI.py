import unittest

import sys
from PyQt5.QtWidgets import (QApplication)
from GameUI import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.test_app = QApplication(sys.argv)
        self.g1 = Game(3, False)

    def tearDown(self):
        pass

    # start 함수가 self.mark를 'O'으로 하고 self.sw 1로 잘 세팅하는지 테스트
    def testStart(self):
        self.g1.mark = 'X'
        self.g1.start()
        self.assertEqual(self.g1.sw, 1)
        self.assertEqual(self.g1.mark, 'O')

    # reset 함수가 self.arr를 잘 초기화 시키는지 테스트
    def testReset(self):
        self.g1.reset()
        for r in range(3):
            for c in range(3):
                self.assertEqual(self.g1.arr[r][c].text(), '')

    # Chk 함수가 self.mark를 매 턴마다 잘 바꾸는지
    # 클릭한 위치에 알맞는 모양을 잘 넣는지
    # 이미 모양이 있는 곳을 클릭했을 시 무효로 잘 처리하는지 테스트
    def testChk(self):
        self.g1.sw = 1
        self.g1.mark = 'O'
        self.g1.chk(0, 0, False)
        self.assertEqual(self.g1.win[0][0], 'O')
        self.assertEqual(self.g1.mark, 'X')
        self.g1.chk(1, 0, False)
        self.assertEqual(self.g1.win[1][0], 'X')
        self.assertEqual(self.g1.mark, 'O')
        self.g1.chk(0, 1, False)
        self.assertEqual(self.g1.win[0][1], 'O')
        self.assertEqual(self.g1.mark, 'X')
        self.g1.chk(0, 0, False)
        self.assertEqual(self.g1.win[0][0], 'O')
        self.assertEqual(self.g1.mark, 'X')


    # 가로, 세로, 대각선 확인해서 승리 조건이 있으면 self.sw를 0으로 잘 세팅하는지
    # 이긴 조건이 없는 상태에서 비어 있는 버튼이 없을 시 비김으로 판단해서 self.sw를 0으로 잘 세팅하는지 테스트
    def testChecking(self):
        self.g1.mark = 'O'
        self.g1.index = 3

        self.g1.win = [['O', 'O', 'O'], ['X', 'X', ''], ['', '', '']]
        self.g1.Checking()
        self.assertEqual(self.g1.sw, 0)

        self.g1.win = [['O', 'X', ''], ['O', 'X', ''], ['O', '', '']]
        self.g1.Checking()
        self.assertEqual(self.g1.sw, 0)

        self.g1.win = [['O', 'X', ''], ['X', 'O', ''], ['', '', 'O']]
        self.g1.Checking()
        self.assertEqual(self.g1.sw, 0)

        self.g1.win = [['', 'X', 'O'], ['X', 'O', ''], ['O', '', '']]
        self.g1.Checking()
        self.assertEqual(self.g1.sw, 0)


        self.g1.win = [['O', 'X', 'O'], ['O', 'X', 'O'], ['X', 'O', 'X']]
        self.g1.Checking()
        self.assertEqual(self.g1.sw, 0)

        self.g1.sw = 1
        self.g1.win = [['O', 'X', ''], ['O', 'X', ''], ['', '', 'O']]
        self.g1.Checking()
        self.assertEqual(self.g1.sw, 1)

    # self.array는 현재 게임판의 상태를 의미
    # AI가 이길 수 있는 차례에 이기는 위치에다가 모양을 표시하는지
    # 못 막으면 상대가 이기는 상황일 때 잘 막는지 self.breakSwitch의 값을 통해 테스트
    def testAI(self):
        self.g1.sw = 1
        self.g1.mark = 'X'
        self.g1.index = 3

        self.g1.breakSwitch = 0
        self.g1.win = [['O', 'X', ''], ['O', 'X', ''], ['', '', 'O']]
        self.g1.AICheckingMark(self.g1.win, 0, 2)
        self.assertEqual(self.g1.breakSwitch, 0)
        self.g1.AICheckingMark(self.g1.win, 2, 1)
        self.assertEqual(self.g1.breakSwitch, 1)

        self.g1.breakSwitch = 0
        self.g1.win = [['X', 'O', ''], ['', 'O', ''], ['', '', '']]
        self.g1.AIDefenseMark(self.g1.win, 0, 2)
        self.assertEqual(self.g1.breakSwitch, 0)
        self.g1.AIDefenseMark(self.g1.win, 2, 1)
        self.assertEqual(self.g1.breakSwitch, 1)

        self.g1.breakSwitch = 0
        self.g1.win = [['', 'O', ''], ['', '', ''], ['', '', '']]
        self.g1.AICheckingMark(self.g1.win, 0, 0)
        self.assertEqual(self.g1.breakSwitch, 0)
        self.g1.AIDefenseMark(self.g1.win, 0, 0)
        self.assertEqual(self.g1.breakSwitch, 0)

if __name__ == '__main__':
    unittest.main()