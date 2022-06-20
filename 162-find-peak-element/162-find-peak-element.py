class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        m = (len(nums)-1)//2
        while m<h:
            if nums[m+1]>nums[m]:
                l = m+1
                m = (l+h)//2
            else:
                h = m
                m = (l+h)//2
        return m