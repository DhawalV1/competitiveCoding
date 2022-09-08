class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if len(nums)%2==0:
            median = (nums[n//2-1]+nums[n//2])//2
        else:
            median = nums[n//2]
        sumi = 0
        for i in nums:
            if i < median:
                sumi = sumi + (median-i)
            else:
                sumi = sumi + (i-median)
        return sumi
            
        