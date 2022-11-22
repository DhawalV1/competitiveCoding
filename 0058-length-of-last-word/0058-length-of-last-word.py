class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        j = 0
        for i in range(len(s)-1,-1,-1):
            if s[i].isalpha():
                count = 1
                j += 1
            if s[i]==' ' and count == 1:
                return j
                
            
        return j
            
                