class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visits = [[False for i in range(len(board[0]))] for j in range(len(board))]

        start_pos = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    start_pos.append([i, j])
        def validate_pos(i, j, n):
            return i >= 0 and i < len(board) and j >= 0 and j < len(board[0]) and not visits[i][j] and board[i][j] == word[n]
        
       
        def backtrack(i, j , n):

            visits[i][j] = True

            if(n==len(word)-1):
                return True 
            
            
            if validate_pos(i+1, j, n+1):
                if(backtrack(i+1, j, n+1)):
                    return True
                visits[i+1][j] = False
            
            if validate_pos(i-1, j, n+1):
                if(backtrack(i-1, j, n+1)):
                    return True
                visits[i-1][j] = False
            
            if validate_pos(i, j-1, n+1):
                if(backtrack(i, j-1,n+1)):
                    return True
                visits[i][j-1] = False
            
            if validate_pos(i, j+1, n+1):
                if(backtrack(i, j+1, n+1)):
                    return True
                visits[i][j+1] = False
            
            return False
        
        for start in start_pos:
            if(backtrack(start[0], start[1], 0)):
                return True 
            visits[start[0]][start[1]] = False

        return False
        