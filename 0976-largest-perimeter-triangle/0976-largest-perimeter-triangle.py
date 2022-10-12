class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        mini = float('inf')
        for i in range(len(nums)-3,-1,-1):
            if (nums[i]+nums[i+1])<=nums[i+2]:
                continue
            else:
                return nums[i]+nums[i+1]+nums[i+2]
            
        return 0
        