class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        
        l = -1
        res = 0
        for x in sorted(A):
            if l < x:
                l = x
            else:
                l += 1
                res += l - x
                
        return res
        