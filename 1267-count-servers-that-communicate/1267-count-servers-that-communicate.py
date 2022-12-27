class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        
        
        if not (cols and rows):
            return 0

        connected = 0                                 
        points=[]                      
        comps_per_row = [0] * rows     
        comps_per_col = [0] * cols     
        
        for row_i in range(rows):
            for col_i in range(cols):
                if grid[row_i][col_i]:              
                    points.append((row_i,col_i))    
                    comps_per_row[row_i]+=1         
                    comps_per_col[col_i]+=1         
        
       
        for row_i,col_i in points:
            
            if comps_per_row[row_i]>1 or comps_per_col[col_i]>1 :
                
                connected += 1                      
        
        return connected