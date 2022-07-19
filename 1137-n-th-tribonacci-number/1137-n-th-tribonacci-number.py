class Solution:
    
    def tribonacci(self, n: int) -> int:
        a = 0
        b = 1
        c = 1
        if n == 0:
            return a
        if n == 1:
            return b
        if n == 2:
            return c
        dp = [-1]*(n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        
        for i in range(3,n+1):
            dp[i] = dp[i-3]+dp[i-2]+dp[i-1]
        
        return dp[-1]
        
        