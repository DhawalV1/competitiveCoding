class Solution:
    def numberOfMatches(self, n: int) -> int:
        
        count = 0
        
        while n!=1:
        
            if n%2==0:
                count += n//2
                n = n//2

            else:

                count += (n-1)//2
                n = (n+1)//2
                
        return count
            
    