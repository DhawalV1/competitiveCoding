class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        
        p = n

        i = 0
        
        while sum(map(int, str(n)))>target:
            
            n = n//10 + 1
            
            i += 1
            
        return n*10**i-p
    
            
        
        
            
            
            
            
        
        
        
        