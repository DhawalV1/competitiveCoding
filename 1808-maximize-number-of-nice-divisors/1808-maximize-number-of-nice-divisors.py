class Solution:
    def maxNiceDivisors(self, p: int) -> int:
        if p == 1: return 1
        
        if p == 2: return 2
        
        mod = 1000000007
        a = p//3
        b = p%3
        
        if b == 0:
            
            return pow(3,a,mod)
        
        elif b == 1:
            
            return pow(3,a-1,mod)*4%mod
        
        else:
            
            return pow(3,a,mod)*2%mod