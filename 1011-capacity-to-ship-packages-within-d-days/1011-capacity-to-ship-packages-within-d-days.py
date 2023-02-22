class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        sumi = sum(weights)
        
        
        
        mini = max(weights)
        
        while mini < sumi:
            
            mid = (sumi+mini)//2
            cur = 0
            need = 1
            
            for w in weights:
                
                if cur + w > mid:
                    cur = 0
                    need += 1
                cur += w
                
            if need > days: 
                mini = mid+1
            else:
                
                sumi = mid
                
        return mini
            
        
        