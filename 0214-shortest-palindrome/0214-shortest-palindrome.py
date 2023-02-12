class Solution:
    def shortestPalindrome(self, s: str) -> str:
        
        longest_palin_idx = 0
        s1 = ''
        s2 = ''
        for i, c in enumerate(s):
            s1 = s1 + c
            s2 = c + s2
            
            if s1 == s2:
                longest_palin_idx = i
        
        return ''.join(reversed(s[longest_palin_idx+1:])) + s