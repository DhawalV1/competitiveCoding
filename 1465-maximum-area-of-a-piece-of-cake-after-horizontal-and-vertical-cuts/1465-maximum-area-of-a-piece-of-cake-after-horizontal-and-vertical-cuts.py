class Solution:
    def maxArea(self, h: int, w: int, ho: List[int], v: List[int]) -> int:
        
        diff1 = 0
        diff2 = 0
        ho = [0] + ho + [h]
        v = [0] + v + [w]
        ho.sort()
        v.sort()
        a = ho[0]
        b = v[0]
        mod = 1000000007
        for i in ho[1:]:
            diff1 = max(diff1,abs(i-a))
            a = i
            
        for i in v[1:]:
            diff2 = max(diff2,abs(i-b))
            b = i
            
        return (diff1*diff2)%mod