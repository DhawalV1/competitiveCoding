class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        ns = int(n**(1/2))
        if k > 2*ns:
            return -1
        factors = []
        for j in range(1,ns+1):
            if n%j==0:
                factors.append(j)
                if j != n/j:
                    factors.append(int(n/j))
        factors.sort()
        return -1 if len(factors)<k else factors[k-1]
            
        