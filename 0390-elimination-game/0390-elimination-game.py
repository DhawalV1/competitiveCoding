class Solution:
    def lastRemaining(self, n: int) -> int:
        def eli(n,isleft):
            
            if n == 1: return 1
            if isleft:
                return 2*eli(n//2,0)
            elif n%2==1:
                return 2*eli(n//2,1)
            else:
                return 2*eli(n//2,1)-1
                
        return eli(n,1)
        
                
                
            
        
        