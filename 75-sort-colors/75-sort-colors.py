class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l = 0
        r = len(nums)-1
        m = 0
        while m <= r:
            if nums[m] == 0:
                nums[l],nums[m] = nums[m],nums[l]
                l = l + 1
                m = m + 1
            elif nums[m] == 1:
                m = m + 1
            else:
        
                nums[r],nums[m] = nums[m],nums[r]
                r = r - 1
        return nums 
                
                
        
        
        