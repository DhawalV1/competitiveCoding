class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')]*(10001)
        coins.sort
        self.helper(coins,amount,dp)
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]
    
    def helper(self,coins,amount,dp):
        dp[0] = 0
        for i in range(10001):
            for j in range(len(coins)):
                if coins[j] <= i:
                    if dp[i-coins[j]]!=float('inf'):
                        dp[i] = min(dp[i],dp[i-coins[j]]+1)
        