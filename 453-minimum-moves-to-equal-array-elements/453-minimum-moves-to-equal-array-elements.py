class Solution:
    def minMoves(self, nums: List[int]) -> int:
        count = 0
        p = min(nums)
        for i in range(len(nums)):
            count += nums[i] - p
            
        return count
        
            
        
        