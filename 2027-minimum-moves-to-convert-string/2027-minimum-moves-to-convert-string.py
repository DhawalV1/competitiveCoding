class Solution:
    def minimumMoves(self, s: str) -> int:
        s += 'OOO'
        count = 0
        i = 0
        while i<len(s)-2:
            if s[i]=='O':
                i += 1
                continue
                
            else:
                
                
                count += 1
                i +=3
                
                    
        return count
                
        