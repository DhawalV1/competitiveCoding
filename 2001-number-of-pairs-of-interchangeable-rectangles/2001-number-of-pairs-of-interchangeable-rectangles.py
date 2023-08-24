class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ans = 0
        ratio = {}
        
        for i,j in rectangles:
            m = i/j
            if m in ratio:
                ratio[m] += 1
                
            else:
                ratio[m] = 1
                
        for key in ratio.keys():
            l = ratio[key]
            ans += l*(l-1)/2
            
        return int(ans)
        