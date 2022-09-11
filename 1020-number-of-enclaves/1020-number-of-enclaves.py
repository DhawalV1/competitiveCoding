class Solution:
    def numEnclaves(self, board: List[List[int]]) -> int:
        
        
        
        count = 0
        
        m = len(board)
        if m == 0:
            return
        n = len(board[0])
        
        for i in range(m):
            for j in range(n):
                if board[i][j]==1:
                    count += 1
        
        for i in range(m):
            if board[i][0] == 1:
                self.dfs(board,i,0,m,n)
                
            if (board[i][n-1] == 1):
                self.dfs(board,i,n-1,m,n)
                
        for j in range(n):
            if board[0][j] == 1:
                self.dfs(board,0,j,m,n)
            if board[m-1][j]==1:
                self.dfs(board,m-1,j,m,n)
                
        for i in range(m):
            for j in range(n):
                if board[i][j]==1:
                    board[i][j] =0
                if board[i][j]=='#':
                    board[i][j] =1
                    
        count2 = 0
        for i in range(m):
            for j in range(n):
                if board[i][j]==1:
                    count2 += 1
        return count - count2
        
    def dfs(self,board,i,j,m,n):
        if i<0 or j<0 or i>=m or j>=n or board[i][j]!=1:
            return 
        board[i][j] = "#"
        self.dfs(board,i-1,j,m,n)
        self.dfs(board,i+1,j,m,n)
        self.dfs(board,i,j-1,m,n)
        self.dfs(board,i,j+1,m,n)
        