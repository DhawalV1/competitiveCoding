class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        count = 0
        dp = 0
        for i in range(2, length):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp += 1
                count += dp
            else:
                dp = 0
        return count
        