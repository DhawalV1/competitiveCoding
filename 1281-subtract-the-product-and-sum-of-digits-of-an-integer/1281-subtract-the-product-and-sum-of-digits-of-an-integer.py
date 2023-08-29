class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sumi = 0
        prod = 1
        while n>0:
            p = n%10
            sumi += p
            prod *= p
            n = n//10
        return prod - sumi