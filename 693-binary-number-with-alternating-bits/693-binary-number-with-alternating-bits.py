class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        r = n ^ (n>>2)
        return bin(r).count('1')==1