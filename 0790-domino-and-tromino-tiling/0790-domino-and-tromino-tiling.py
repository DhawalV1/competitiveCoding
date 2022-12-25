class Solution:
    def numTilings(self, n: int) -> int:
        
        mod = 1000000007
        dp = [0]*(n+3)
        dp[0] = 1
        dp[1] = 2
        dp[2] = 5
        for i in range(3,n):
            
            dp[i] = (2*dp[i-1] + dp[i-3])%mod
            
        return dp[-4]