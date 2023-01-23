class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        k = 0
        p = ''
        i = 0
        while i < len(s)+len(spaces) and k<len(spaces):
            
            if i == spaces[k]:
                
                p += ' '
                spaces[k] -= 1
                i -= 1
                k += 1
            else:
                
                p += s[i]
            i += 1
                
        p += s[spaces[-1]+1:]
        return p
            