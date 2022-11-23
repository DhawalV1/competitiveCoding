class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        NR = len(grid)
        NC = len(grid[0])
        vec = [0] * NR * NC 
        k = k % (NR * NC)  
        
		
        for i in range(NR):
            for j in range(NC):
                vec[i * NC + j] = grid[i][j]
				
        
        vec = vec[-k:] + vec[:-k]
		
   
        for i in range(NR):
            for j in range(NC):
                grid[i][j] = vec[i * NC + j]
        return grid