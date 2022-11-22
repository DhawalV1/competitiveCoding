class Solution:
    def isPalindrome(self, s: str) -> bool:
        print(ord('A'),ord('a'))
        p = ''
        for i in range(len(s)):
            if s[i].isalpha() or s[i].isdigit():
                if 65<=ord(s[i])<=90:
                    p += chr(32+ord(s[i]))
                else:
                    p += s[i]
            else:
                continue
        return p==p[::-1]
        
       