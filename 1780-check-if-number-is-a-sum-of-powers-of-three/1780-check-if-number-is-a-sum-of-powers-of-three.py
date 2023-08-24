class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        
        
            
        while n>0:
            
            if n%3==1:
                n = n-1
            elif n%3==2:
                return False
            else:
                n = n/3
                
        return True
        