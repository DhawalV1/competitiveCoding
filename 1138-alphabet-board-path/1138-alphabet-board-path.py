class Solution:
    def alphabetBoardPath(self, t: str) -> str:
        
        m = {c:[i//5,i%5] for i,c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        
        x0 = 0
        y0 = 0
        
        res = []
        
        for c in t:
            x,y = m[c]
            if y < y0: res.append('L' * (y0 - y))
            if x < x0: res.append('U' * (x0 - x))
            if x > x0: res.append('D' * (x - x0))
            if y > y0: res.append('R' * (y - y0))
            res.append('!')
            x0,y0 = x,y
            
        return "".join(res)
        
        
        """
        m = {c: [i / 5, i % 5] for i, c in enumerate("abcdefghijklmnopqrstuvwxyz")}
        x0, y0 = 0, 0
        res = []
        for c in target:
            x, y = m[c]
            if y < y0: res.append('L' * (y0 - y))
            if x < x0: res.append('U' * (x0 - x))
            if x > x0: res.append('D' * (x - x0))
            if y > y0: res.append('R' * (y - y0))
            res.append('!')
            x0, y0 = x, y
        return "".join(res)
            
        """
        