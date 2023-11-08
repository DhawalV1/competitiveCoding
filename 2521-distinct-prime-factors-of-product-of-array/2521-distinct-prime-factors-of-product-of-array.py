class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        ans = set()
        for i in nums:
            
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    ans.add(j)
                    while i % j == 0:
                        i //= j
            if i >= 2:
                ans.add(i)
        return len(ans) 
        