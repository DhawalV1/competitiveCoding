class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        mod = 10**9 + 7
        arr.sort()
        dp = {}
        
        for a in arr:
            dp[a]=1
            
        for index,a in enumerate(arr):
            for b in arr[0:index]:
                if a%b == 0:
                    key = int(a/b)
                    if key in dp:
                        dp[a] += dp[b]*dp[key]
                        
        return sum(dp.values())%mod
                    
                

        