class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def helper(m,n):
            if (m,n) in memo:
                return memo[(m,n)]
            
            if m==1 or n==1:
                memo[(m,n)] = 1
                return 1
            
            res = helper(m-1,n) + helper(m,n-1)
            memo[(m,n)] = res
             
                
            return res
        return helper(m,n)
            
        
        