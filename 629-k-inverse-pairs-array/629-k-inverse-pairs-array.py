class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        dp = [[0] * 1001 for _ in range(1001)]
        dp[0][0] = 1
        
        mod = (10 ** 9) + 7
        
        if dp[n][k] != 0:
            return dp[n][k]
        else:
            for N in range(1, n + 1):
                for K in range(k + 1):
                    if K > 0:
                        dp[N][K] = (dp[N - 1][K] + dp[N][K - 1]) % mod
                    else:
                        dp[N][K] = (dp[N - 1][K]) % mod
                    
                    if K >= N:
                        dp[N][K] = (dp[N][K] - dp[N - 1][K - N]) % mod
            
            
            return dp[n][k]
        