class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxi = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    maxi = max(maxi,self.dfs(grid,i,j))
        return maxi
    
    def dfs(self,grid,i,j):
        if 0<=i<len(grid) and 0<=j<len(grid[0]) and grid[i][j]==1:
            grid[i][j] = 0
            return 1 + self.dfs(grid,i+1,j) +  self.dfs(grid,i-1,j) +  self.dfs(grid,i,j+1) +  self.dfs(grid,i,j-1)
        
        return 0