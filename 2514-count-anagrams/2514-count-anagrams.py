class Solution:
    def countAnagrams(self, s: str) -> int:
        prod = 1
        mod = 10**9+7
        words = list(s.split(' '))
        for w in words:
            prem = math.factorial(len(w))
            for val in collections.Counter(w).values():
                prem = prem//(math.factorial(val))
            prod = prod*prem%mod
                
        return prod
                