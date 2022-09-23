class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return self.helper(n)
    def helper(self,n):
        mod = 10**9 + 7
        if n == 1:
            return 1
        p = bin(n)[2:]
        
        return (self.helper(n-1)<<len(p))%mod + n
        