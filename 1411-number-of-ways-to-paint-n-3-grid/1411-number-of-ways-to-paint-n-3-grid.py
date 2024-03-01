class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9+7
        col1 = 6
        col2 = 6
        for i in range(n-1):
            temp = col1
            col1 = (col1*2%mod+col2*2%mod)%mod
            col2 = (temp*2%mod+col2*3%mod)%mod
        return (col1+col2)%mod