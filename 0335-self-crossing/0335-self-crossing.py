class Solution:
    def isSelfCrossing(self, x: List[int]) -> bool:
        
        a, b, c, d, e, f = [-1] * 6
        for z in x:
          f, e, d, c, b, a = e, d, c, b, a, z
          if d >= 0 and (c <= a) and (d >= b):
            return True
          if e >= 0 and (c > a) and (d == b) and (e >= c - a):
            return True
          if f >= 0 and (c > a) and (d > b) and (e >= c - a and e <= c) and (f >= d - b):
            return True
        return False
