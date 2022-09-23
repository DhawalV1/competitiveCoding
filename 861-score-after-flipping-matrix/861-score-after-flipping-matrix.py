class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            if grid[i][0]==0:
                for j in range(n):
                    
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                    else:
                        grid[i][j] = 0
                        
        for i in range(n):
            sumi = 0
            for j in range(m):
                sumi += grid[j][i]
            if 2*sumi<m:
                for k in range(m):
                    if grid[k][i]==0:
                        grid[k][i] = 1
                    else:
                        grid[k][i]=0
                    
                    
        res = 0
        for i in range(m):
            ans = 0
            for j in range(n-1,-1,-1):
                if grid[i][j]:
                    ans += 2**(n-1-j) 
            
            res += ans 
        print(grid)
        return res
        