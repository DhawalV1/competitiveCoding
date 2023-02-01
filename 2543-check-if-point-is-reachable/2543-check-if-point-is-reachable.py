class Solution:
    def isReachable(self,x: int,y: int) -> bool:
        
        v = math.gcd(x, y)
        return v == (v & -v)