class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row = len(image)
        col = len(image[0])
        change = image[sr][sc]
        
        
        def dfs(r,c):
            nonlocal row,col,image,color
            if r<0 or c<0 or r>row-1 or c>col-1 or image[r][c] == color or image[r][c]!=change:
                return
            
            image[r][c] = color
            
            dfs(r,c+1)
            dfs(r,c-1)
            
            dfs(r+1,c)
            dfs(r-1,c)
            
        dfs(sr,sc)
        
        return image
        
        