class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        def dfs(r):
            if r == n:
                res.append([''.join(row) for row in b])
                return
            
            for c in range(n):
                if isval(r,c):
                    b[r][c] = 'Q'
                    dfs(r+1)
                    b[r][c] = '.'
                    
        def isval(r,c):
            
            for i in range(r):
                for j in range(n):
                    
                    if b[i][j] == 'Q' and (c==j or r+c==i+j or r-c==i-j):
                        
                        return False
            return True
                
            
            
            
            
        b = [['.']*n for i in range(n)]
        res = []
        dfs(0)
        return res
    
    
        