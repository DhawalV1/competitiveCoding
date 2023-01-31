class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        
        def countislands(grid):
            islands = 0
            visited = set()

            def dfs(grid,row,col,visited):
                if 0 <= row < len(grid) and 0 <= col < len(grid[0]) and grid[row][col] == 1 and (row,col) not in visited:
                    visited.add((row,col))
                    dfs(grid,row+1,col,visited)
                    dfs(grid,row-1,col,visited)
                    dfs(grid,row,col+1,visited)
                    dfs(grid,row,col-1,visited)


            for row in range(len(grid)):
                for col in range(len(grid[0])):
                    if grid[row][col] == 1 and (row,col) not in visited:
                        islands += 1
                        dfs(grid,row,col,visited)
            
            return islands
        
        if countislands(grid) != 1:
            return 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    grid[i][j] = 0
                    if countislands(grid) != 1:
                        return 1
                    grid[i][j] = 1
        return 2