class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        sumi = 0
        change = 0
        mx_far = -1*nums[0]
        mx_end = 0
        mx_far1 = nums[0]
        mx_end1 = 0
        ahh = nums[0]
        for i in range(len(nums)):
            
            if nums[i] >= 0:
                change = 1
                
            ahh = max(ahh,nums[i])
                
            
            mx_end1 = mx_end1 + nums[i]
            if mx_far1 < mx_end1:
                mx_far1 = mx_end1
            if mx_end1 < 0:
                mx_end1 = 0
            
            mx_end = mx_end - nums[i]
            if mx_far < mx_end:
                mx_far = mx_end
            if mx_end < 0:
                mx_end = 0
                
            sumi += nums[i]
            
        if change == 0: return ahh
            
        return max(mx_far1,sumi+mx_far)
        