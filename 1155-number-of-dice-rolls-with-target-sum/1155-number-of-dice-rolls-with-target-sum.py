class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        
        memo = {}
        def dp(n,target):
            if n == 0:
                return 0 if target > 0 else 1
            if (n,target) in memo:
                return memo[(n,target)]
            
            ret = 0
            
            for l in range(max(0,target-k),target):
                ret += dp(n-1,l)
                
            memo[(n,target)] = ret
            return ret
        
        return dp(n,target) % (10**9 + 7)
        
        
        