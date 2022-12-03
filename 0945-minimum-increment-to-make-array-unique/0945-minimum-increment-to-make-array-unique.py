class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        
        level = -1 
        res = 0
        
        for x in sorted(A):
            if level < x:
                level = x
            else:
                level += 1
                res += level - x
        
        return res
            
        