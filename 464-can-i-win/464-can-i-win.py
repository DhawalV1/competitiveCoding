class Solution:
    def canIWin(self, maxi: int, total: int) -> bool:
        @lru_cache(None)
        def r(s, t):
            if sum(s) < t: return False
            if t <= max(s): return True
            if sum(s) == t: return len(s)%2 == 1
            return any(not r(s[:i] + s[i+1:], t-s[i]) for i in range(len(s))[::-1])
        return r(tuple(range(1, maxi + 1)),total)
         
        
        
        
      
    
            
        