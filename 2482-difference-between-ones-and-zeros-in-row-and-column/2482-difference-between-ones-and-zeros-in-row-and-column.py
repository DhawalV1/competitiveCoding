class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        
        m = len(grid)
        n = len(grid[0])
        rowone = [0]*m
        colone = [0]*n
        for i in range(m):
            for j in range(n):
                rowone[i] += grid[i][j]
                colone[j] += grid[i][j]
                
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2*rowone[i] + 2*colone[j] - m - n
                
        return grid
        
                