class Solution:
    def concatenatedBinary(self, n: int) -> int:
        #return self.helper(n)
        mod = 10**9 + 7
        ans = 0
        
        for i in range(1,n+1):
            b = math.floor(math.log2(i))+1
            ans = ((ans<<b)%mod + i)%mod
            
        return ans
    ''''
    def helper(self,n):
        mod = 10**9 + 7
        if n == 1:
            return 1
        p = bin(n)[2:]
        
        return (self.helper(n-1)<<len(p))%mod + n
    '''