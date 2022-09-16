import numpy as np
class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def win(board,c):
            for line in board:
                if line[0]==line[1]==line[2]==c:return True
            for col in range(3):
                if board[0][col]==board[1][col]==board[2][col]==c:return True
            if board[0][0]==board[1][1]==board[2][2]==c:return True
            if board[0][2]==board[1][1]==board[2][0]==c:return True
            return False
        c=collections.Counter(''.join(board))
        xc,oc=c['X'],c['O']
        if xc<oc or xc>oc+1:return False
        if win(board,'X') and oc!=xc-1:return False
        if win(board,'O') and oc!=xc:return False
        return True
        