class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        
        a,b,c,d = rec1
        e,f,g,h = rec2
        if min(c,g) - max(a,e) > 0 and min(d,h) - max(b,f) > 0:
            return True
        return False