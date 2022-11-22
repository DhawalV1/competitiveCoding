class Solution:
    def titleToNumber(self, s: str) -> int:
        p = (ord(s[0])-64)
        for i in range(1,len(s)):
            p = p*26 + (ord(s[i])-64)
        return p
        