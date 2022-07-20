class Solution:
    def superEggDrop(self, n: int, k: int) -> int:
        
        low = 1
        high = k

        # Do binary search, for every
        # mid, find sum of binomial
        # coefficients and check if
        # the sum is greater than k or not.
        while (low < high):

            mid = int((low + high) / 2)
            if (self.binomialCoeff(mid, n, k) < k):
                low = mid + 1
            else:
                high = mid

        return int(low)

        
    
    
    
    def binomialCoeff(self,x, n, k):
 
        sum = 0
        term = 1
        i = 1
        while(i <= n and sum < k):
            term *= x - i + 1
            term /= i
            sum += term
            i += 1
        return sum
        