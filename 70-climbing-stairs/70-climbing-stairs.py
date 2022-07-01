class Solution:
    def climbStairs(self, n: int) -> int:
        
        cache = {}
        
        def helper(n):
            
            if n in cache:
                return cache[n]
            
        
    
            if n == 1:
                res =  1
            elif n == 2:
                res = 2
            else:
                res = helper(n-1) + helper(n-2)
                
            
        
            cache[n] = res
            return res
        return helper(n)
            
        