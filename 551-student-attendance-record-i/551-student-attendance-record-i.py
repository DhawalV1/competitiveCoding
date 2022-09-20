class Solution:
    def checkRecord(self, s: str) -> bool:
        s = s + 'PP'
        count = 0
        for i in range(len(s)-2):
            if s[i] == 'A':
                count += 1
                if count > 1:
                    return False
                    
            elif s[i]=='L':
                if s[i+1]=='L':
                    if s[i+2]=='L':
                        return False
            else:
                continue
        return True