class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        mini = min(nums)
        maxi = max(nums)
        
        for i in nums:
            if i!=mini and i!=maxi:
                return i
        return -1