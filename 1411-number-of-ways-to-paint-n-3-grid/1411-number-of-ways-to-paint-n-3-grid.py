class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9+7
        a = [[6,6]]
        for i in range(n-1):
            a.append([(a[i][0]*2%mod+a[i][1]*2%mod)%mod,(a[i][0]*2%mod+a[i][1]*3%mod)%mod])
        return sum(a[-1])%mod