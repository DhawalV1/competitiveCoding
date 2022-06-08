class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        for start in range(len(nums)):
            if start > end:
                return False
            step = nums[start]
            end = max(end, start + step)
        return True
        