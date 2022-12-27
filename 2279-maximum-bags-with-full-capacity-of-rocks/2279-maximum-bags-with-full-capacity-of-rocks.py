class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], ad: int) -> int:
        
        empty = []
        
        for i in range(len(capacity)):
            
            empty.append(capacity[i]-rocks[i])
            
        empty.sort()
        count = 0
        for l in empty:
            
            if l == 0: count += 1
                
            else:
                
                ad -= l
                
                if ad>=0:
                    
                    count += 1
                    
                else:
                    
                    return count
                
        
        return count
        