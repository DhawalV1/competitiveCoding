class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        m = len(nums)
        return int(m*(m+1)/2 - sum(nums))
        