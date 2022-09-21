class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        
        res = 0
        for i in range(len(nums)):
            sm = nums[i]
            lg = nums[i]
            for j in range(i+1,len(nums)):
                sm = max(sm,nums[j])
                lg = min(lg,nums[j])
                
                res += sm-lg
                
        return res
        
        