class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mx_far = nums[0]
        mx_end = 0
        for i in range(len(nums)):
            mx_end = mx_end + nums[i]
            
            if mx_far < mx_end:
                mx_far = mx_end
            if mx_end < 0:
                mx_end = 0
        return mx_far
        