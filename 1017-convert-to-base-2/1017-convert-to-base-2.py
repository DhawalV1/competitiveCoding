class Solution:
    def baseNeg2(self, x: int) -> str:
        res = []
        while x:
            res.append(x & 1)
            x = -(x >> 1)
        return "".join(map(str, res[::-1] or [0]))

        