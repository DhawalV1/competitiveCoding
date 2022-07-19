class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        dp = [-1]*(n+1)
        dp[0] = 0
        dp[1] = 1
        maxi = -2
        for i in range(2,n+1):
            if i%2==0:
                dp[i] = dp[i//2]
            else:
                dp[i] = dp[(i-1)//2] + dp[(i-1)//2+1]
            maxi = max(dp[i],maxi)
            
        return maxi
        
            
        