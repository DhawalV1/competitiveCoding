class Solution:
    def twoEggDrop(self, n: int) -> int:
        if n <= 2:
            return n
        i = int(sqrt(2*n))
        while i < n:
            if i*(i+1)>=2*n:
                return i
            i = i+1
        