class Solution:
    def minAddToMakeValid(self, p: str) -> int:
        r, l = 0, []
        for s in p:
            if s == "(":
                l.append(s)
            elif l:
                l.pop()
            else:
                r += 1 
        return r + len(l)
    
        