class Solution:
    def minFallingPathSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        
        
        for i in range(1,n):
            # mat[i][0] = min(mat[i-1][0],mat[i-1][1])
            # mat[i][-1] = min(mat[i-1][-1],mat[i-1][-2])
            for j in range(n):
                mat[i][j] = mat[i][j] + min(mat[i-1][k] if k!=j else float('inf') for k in range(n)) 
        return min(mat[-1])
