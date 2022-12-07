class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        
        ones = nums.count(1)
        nums = nums + nums[0:ones]
        onesin = nums[0:ones].count(1)
        mini = float('inf')
        for i in range(ones,len(nums)):
            onesin = onesin + nums[i] - nums[i - ones]
            mini = min(mini,ones - onesin)
        return mini
    
            