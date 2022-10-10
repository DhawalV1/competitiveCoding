class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        
        row = []
        col = []
        for i in range(len(grid)):
            row.append(max(grid[i]))
        for i in range(len(grid[0])):
            maxi = 0
            for j in range(len(grid)):
                maxi = max(maxi,grid[j][i])
            col.append(maxi)
        sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                sum += min(row[i],col[j])-grid[i][j]
                
        return sum
                
        