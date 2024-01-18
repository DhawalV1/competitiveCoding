class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        cache = {}
        
        def helper(n):
            
            if n in cache:
                return cache[n]
            
        
    
            if n <3:
                res =  n
            
            else:
                res = helper(n-1) + helper(n-2)
                
            
        
            cache[n] = res
            return res
        return helper(n)
        ''' 
        if n<3:
            return n
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2
        for i in range(2,n):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n-1]