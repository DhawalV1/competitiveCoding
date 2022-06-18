class Solution:
    def reverse(self, x: int) -> int:
        if x>=0:
            p = str(x)
            p = p[::-1]
            r = int(p)
            if r>2147483647:
                return 0
            else:
                return r
        else:
            p = str(-x)
            p = p[::-1]
            r = int(p)
            if r>2147483648:
                return 0
            else:
                return -r