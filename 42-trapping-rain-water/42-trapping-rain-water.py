class Solution:
    def trap(self, b: List[int]) -> int:
        if not b or len(b)<3:
            return 0
        vol = 0
        l,r = 0,len(b)-1
        lmax,rmax = b[l],b[r]
        while l<r:
            lmax,rmax = max(lmax,b[l]),max(rmax,b[r])
            
            if lmax <= rmax:
                vol += lmax-b[l]
                l += 1
            else:
                vol += rmax - b[r]
                r -= 1
        return vol
        