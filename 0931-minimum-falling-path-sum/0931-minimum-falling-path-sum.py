class Solution(object):
    def minFallingPathSum(self, mat):
        n = len(mat)
        for i in range(n):
            mat[i] = [float('inf')]+mat[i]+[float('inf')]
        
        for i in range(1,n):
            # mat[i][0] = min(mat[i-1][0],mat[i-1][1])
            # mat[i][-1] = min(mat[i-1][-1],mat[i-1][-2])
            for j in range(1,n+1):
                mat[i][j] = mat[i][j] + min(mat[i-1][j-1],mat[i-1][j],mat[i-1][j+1])
        return min(mat[-1])

    
    
