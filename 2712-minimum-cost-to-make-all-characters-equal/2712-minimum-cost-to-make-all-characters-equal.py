class Solution:
    def minimumCost(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(1,len(s)):
            
            if s[i]!=s[i-1]:
                ans += min(i,n-i)
        
        return ans