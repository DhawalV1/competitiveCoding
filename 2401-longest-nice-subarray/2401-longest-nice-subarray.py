class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        i = 0
        res = 0
        andi = 0
        for j in range(len(nums)):
            
            while nums[j] & andi:
                
                andi ^= nums[i]
                i += 1
            andi |= nums[j]
            res = max(res,j-i+1)
            
            
        return res
                
            
            
            
        