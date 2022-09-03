class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        if n==1:
            return True
        m = str(n)
        o = [int(i) for i in m]
        o.sort()
        p = len(str(n))
        q = 1 << 0
        while len(str(q))<p+1:
            q = q << 1
            if len(str(q)) == p:
                r = str(q)
                y = [int(i) for i in r]
                y.sort()
                if y == o:
                    return True
        return False
        
        
        