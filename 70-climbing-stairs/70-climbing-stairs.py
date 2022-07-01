class Solution:
    def climbStairs(self, n: int) -> int:
        
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
            
        