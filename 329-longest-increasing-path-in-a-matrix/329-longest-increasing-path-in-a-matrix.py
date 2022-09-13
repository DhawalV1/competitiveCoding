class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        @lru_cache(None)
        
        def dfs(i,j):
            ans = 1
            for ni,nj in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
                if 0<=ni<m and 0<=nj<n and matrix[ni][nj] < matrix[i][j]:
                    ans = max(ans,1+dfs(ni,nj))
                    
            return ans
        ans = 1
        for i in range(m):
            for j in range(n):
                ans = max(ans,dfs(i,j))
                
        return ans
        
        
        
        