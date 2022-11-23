class Solution(object):
    def isValidSudoku(self, board):
       
        seen = set()
        for i in range(0,9):
            for j in range(0,9):
                if board[i][j]!='.':
                    
                    cur = board[i][j]
                    
                    if (i,cur) in seen or (cur,j) in seen or (i/3,j/3,cur) in seen:
                        return False
                    seen.add((i,cur))
                    seen.add((cur,j))
                    seen.add((i/3,j/3,cur))
                    
        return True
    
        