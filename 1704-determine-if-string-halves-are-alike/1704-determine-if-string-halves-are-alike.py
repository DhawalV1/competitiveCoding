class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        count = count2 = 0
        seen = set(('a','e','i','o','u','A','E','I','O','U'))
        n = len(s)//2
        for i in range(len(s)):
            if i < n:
                if s[i] in seen:
                    count += 1
            else:
                if s[i] in seen:
                    count -= 1
                    
        return count == 0
        