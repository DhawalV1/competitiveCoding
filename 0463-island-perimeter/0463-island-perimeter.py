class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def check(i,j):
            if i>=0 and i<m and j>=0 and j<n and grid[i][j]==1:
                return True
        sumi = 0
        dire = [[0,1],[0,-1],[1,0],[-1,0]]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    sumi += 4
                    for p,q in dire:
                        if check(i+p,j+q):
                            sumi -= 1
                            
        return sumi
                            
                    
            
        