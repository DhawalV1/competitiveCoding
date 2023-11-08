class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        x = abs(sx-fx)
        y = abs(sy-fy)
        if x == 0 and y == 0:
            if t == 1: return False
        return max(x,y)<=t
        