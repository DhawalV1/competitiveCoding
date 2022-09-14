from collections import defaultdict
class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prevsum = defaultdict(lambda:0)
        curr = 0
        res = 0
        for i in range(len(nums)):
            curr += nums[i]
            if curr == goal:
                res += 1
                
            if (curr-goal) in prevsum:
                res += prevsum[curr-goal]
                
            prevsum[curr] += 1
                
        return res