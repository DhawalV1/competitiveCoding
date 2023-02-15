class Solution:
    def minimumPerimeter(self, n: int) -> int:
        
        i = 0
        
        while 2*i*(i+1)*(2*i+1)<n:
            
            i += 1
            
        return i*8
    
    