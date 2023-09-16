class Solution:
    def minimumMoves(self, s: str) -> int:
        s += 'OOO'
        count = 0
        i = 0
        while i<len(s)-2:
            if s[i]=='O':
                i += 1
                continue
                
            elif s[i] == 'X':
                if s[i+1:i+3]=='OO':
                    count += 1
                    i +=3
                elif s[i+1:i+3]=='XO':
                    count += 1
                    i +=3
                elif s[i+1:i+3]=='OX':
                    count += 1
                    i +=3
                else:
                    count += 1
                    i +=3
                    
        return count
                
        