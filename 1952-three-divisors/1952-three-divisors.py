class Solution:
    def isThree(self, n: int) -> bool:
        
        if n<4:return False
        if n == 4: return True
        
        def isprime(m):
            
            for i in range(2,int(m**0.5)+1):
                
                if m%i==0:
                    
                    return False
                
            return True
        
        if int(n**0.5) == n**0.5: return isprime(n**0.5)
        else: return False
        