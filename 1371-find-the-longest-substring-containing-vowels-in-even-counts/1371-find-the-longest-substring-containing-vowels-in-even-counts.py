class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = {'a': 1, 'e': 2, 'i': 4, 'o': 8, 'u': 16}
        r = 0
        d = {0:-1}
        n = 0
        for i,c in enumerate(s):
            if c in vowels:
                n ^= vowels[c]
            if n not in d:
                d[n] = i
                
            else:
                r = max(r,i-d[n])
        
        return r