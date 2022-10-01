class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        maxi = max(nums)
        res = 0
        count = 0
        for n in nums:
            if n == maxi:
                count += 1
                
            else:
                count = 0
                
                
            res = max(res,count)
            
        return res
        
        
        
        