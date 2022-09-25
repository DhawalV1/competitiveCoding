class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if k == 1: return "0"
        if k == 2**(n-1): return "1"
        if k < 2**(n-1): return self.findKthBit(n-1, k)
        if self.findKthBit(n-1, 2**n-k) == "1":
            return '0'
        else:
            return '1' 