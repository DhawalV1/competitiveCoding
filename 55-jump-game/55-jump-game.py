class Solution:
    def canJump(self, nums: List[int]) -> bool:
        end = 0
        for i in range(len(nums)):
            if i > end:
                return False
            steps = nums[i]
            end = max(end, steps + i)
        return True
