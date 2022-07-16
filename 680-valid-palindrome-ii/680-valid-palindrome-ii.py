class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(len(s)//2+1):
            if s[i] != s[len(s)-i-1]:
                return self.helper(s,i) or self.helper(s,len(s)-i-1)
                
    def helper(self,s,i):
        s = s[0:i]+s[i+1:]
        if s == s[::-1]:
            return True
        else:
            return False
        