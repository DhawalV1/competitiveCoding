class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        
        odd = 0
        even = 0
        
        while n>0:
            
            even += n&1 
            
            n = n>>1
            
            odd += n&1
            
            n = n>>1
            print(even,odd,n)
        return [even,odd]
        