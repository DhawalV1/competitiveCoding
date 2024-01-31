class Solution:
    def numWays(self, s: str) -> int:
        n = len(s)
        mod = 10**9+7
        ones = []
        for i in range(n):
            if s[i]=='1':
                ones.append(i)
        tot = len(ones)
        if tot%3!=0:return 0
        if tot==0:return (n-2)*(n-1)//2%mod
        
        return (ones[tot//3]-ones[tot//3-1])*(ones[2*tot//3]-ones[2*tot//3-1])%mod
        