class Solution:
    def reachNumber(self, target: int) -> int:
        if target<0:
            return self.reachNumber(-target)
        if target == 1: return 1
        res = 0
        
        start = 0
        i = 1
        while start < target or (start-target)&1: 
            start += i
            i += 1
            res += 1
            print(start,i)
            
        else:
            return res
            
            