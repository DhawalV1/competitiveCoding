class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:        
        l, r = 0, 0        
        while r < len(nums):
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
            while r < len(nums) and nums[l-1] == nums[r]:
                r +=1
        return l