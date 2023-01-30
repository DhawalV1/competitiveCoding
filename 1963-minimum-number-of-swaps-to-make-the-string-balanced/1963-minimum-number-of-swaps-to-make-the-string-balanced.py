class Solution:
    def minSwaps(self, s: str) -> int:
        
        bal = 0
        swap = 0
        
        for i in s:
            
            if i == '[':
                bal += 1
            else:
                bal -= 1
                if bal == -1:
                    swap += 1
                    bal = 1
                    
        return swap