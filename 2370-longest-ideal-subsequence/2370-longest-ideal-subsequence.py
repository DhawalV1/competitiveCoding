class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        
        dp = [0]*26
        
        for ch in s:
            i = ord(ch) - ord('a')
            
            dp[i] = 1 + max(dp[max(0,i-k):min(i+k+1,26)])
            
        return max(dp)
            