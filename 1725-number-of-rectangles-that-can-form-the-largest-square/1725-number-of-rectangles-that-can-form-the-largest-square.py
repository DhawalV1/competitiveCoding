class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        
        a = [min(i,j) for i,j in rectangles]
        p = max(a)
        return collections.Counter(a)[p]
        