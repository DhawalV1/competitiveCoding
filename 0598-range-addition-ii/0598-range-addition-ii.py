class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if not ops:return m*n
        min1 = 41*10000
        min2 = 41*10000
        
        for i in ops:
            min1 = min(min1,i[0])
            min2 = min(min2,i[1])
            
        return min1 * min2