class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums)<2:
            return 0
        p = 0
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                p += 1
        if p == len(nums)-1:
            return 0
        i = 0
        j = len(nums)-1
        while i < len(nums)-1:
            if nums[i]>nums[i+1]:
                break
            i = i+1
        while j > 0:
            if nums[j] < nums[j-1]:
                break
            j = j-1
        if nums[i:j+1]:
            mini = min(nums[i:j+1])
        
            maxi = max(nums[i:j+1])
        else:
            mini = nums[0]
            maxi = nums[-1]
        start1 = 0
        while start1 < len(nums):
            if nums[start1] > mini:
                n = start1
                break
                
            start1 += 1
        start2 = len(nums)-1
        while start2 > 0:
            if nums[start2] < maxi:
                m = start2
                break
            start2 -= 1
            
        return m-n+1