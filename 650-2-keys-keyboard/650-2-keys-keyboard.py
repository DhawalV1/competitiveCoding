class Solution:
    def minSteps(self, n: int) -> int:
        def factors(n):
            d = 2
            while d * d <= n:
                while n % d == 0:
                    n /= d
                    yield int(d)
                d += 1
            if n > 1:
                yield int(n)

        return sum(factors(n))
            
        