class Solution:
    def arrangeCoins(self, n: int) -> int:
        n *= 2
        m = int(sqrt(n))
        if (m+1)*m<=n: return m
        else: return m-1
        