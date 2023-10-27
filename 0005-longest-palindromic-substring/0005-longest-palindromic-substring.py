class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        start,maxlen = 0,1
        for i in range(0,n):
            right = i
            while right < n and s[i]==s[right]:
                right += 1
                
            left = i-1
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
                
            pallen = right - left - 1
            if pallen > maxlen :
                maxlen = pallen 
                start = left + 1
                
        return s[start:(maxlen+start)]
                
                