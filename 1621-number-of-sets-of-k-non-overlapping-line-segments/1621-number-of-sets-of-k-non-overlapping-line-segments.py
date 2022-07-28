class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        mod  = 10**9 + 7
        @lru_cache(None)
        def dp(i,k,start):
            if k == 0: return 1
            if i == n: return 0
            ans = dp(i+1,k,start)
            if start:
                ans += dp(i+1,k,False)
            else:
                ans += dp(i,k-1,True)
                
            return ans % mod
        
        return dp(0,k,True)
        
        res = 1
        for i in xrange(1, k * 2 + 1):
            res *= n + k - i
            res /= i
        return res % (10**9 + 7)
        