class Solution:
    def maxDistance(self, pos: List[int], m: int) -> int:
        
        pos.sort()
        
        if m == 2: return pos[-1] - pos[0]
        n = len(pos)
        def count(d):
            ans, curr = 1, pos[0]
            for i in range(1, n):
                if pos[i] - curr >= d:
                    ans += 1
                    curr = pos[i]
            return ans

        
        
        l = 0
        r = pos[-1] - pos[0]
        
        while l<r:
            
            mid = r - (r-l)//2
            
            if count(mid)>=m:
                
                l = mid
                
            else:
                
                r = mid - 1
                
        return l
                    
        
        
                
                
                
        
        
        
        
        