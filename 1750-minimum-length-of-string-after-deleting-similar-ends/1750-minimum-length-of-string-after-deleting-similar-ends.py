class Solution:
    def minimumLength(self, s: str) -> int:
        count = 0
        if len(s) == 1: return 1
        for i in range(0,len(s)-1):
            if s[i] == s[i+1]: count += 1
        if count == len(s)-1: return 0
        change = True
        i = 0
        j = len(s)-1
        n = j+1
        if s[i]!=s[j]:return n
        while(s[i]==s[j] and i<j):
            
            while s[i]==s[i+1]:
                i += 1
            if i == j: return 0
            while s[j] == s[j-1]:
                j -= 1
            if j-i==1 and s[j]==s[i]: return 0
            i += 1
            j -= 1

            if j-i==1 and s[j]==s[i]: return 0
                
        return j-i+1
    
    
    "aabccabba"
            
            