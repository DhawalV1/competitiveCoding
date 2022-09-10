class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count
    def dfs(self, grid, x, y):
        if 0<=x<len(grid) and 0<=y<len(grid[0]) and grid[x][y]=='1':
            grid[x][y] = '0'
            self.dfs(grid,x+1,y)
            self.dfs(grid,x-1,y)
            self.dfs(grid,x,y+1)
            self.dfs(grid,x,y-1)
            