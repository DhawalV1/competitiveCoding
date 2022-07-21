class Solution:
    def numTeams(self, rating: List[int]) -> int:
        a = d = 0
        for i,v in enumerate(rating):
            x = y = z = w = 0
            for l in rating[:i]:
                if l < v:
                    x += 1
                if l>v:
                    y += 1
            for l  in rating[i+1:]:
                if l > v:
                    z += 1
                if l < v:
                    w += 1
            a += x*z
            d += y*w
        return a+d
                
        