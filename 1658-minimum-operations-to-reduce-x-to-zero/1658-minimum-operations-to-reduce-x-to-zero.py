class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sumi = sum(nums) - x
        if sumi == 0:
            return len(nums)
        maxlength = -1
        currsum = 0
        l = 0
        for r in range(len(nums)):
            currsum += nums[r]
            while l < r and currsum > sumi:
                currsum -= nums[l]
                l += 1
            if currsum == sumi:
                maxlength = max(maxlength,r-l+1)
                
        if maxlength!= -1:
            return len(nums) - maxlength
        else:
            return -1
        
        
        
       