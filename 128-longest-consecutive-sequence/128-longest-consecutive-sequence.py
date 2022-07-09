class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxi = 0
        mx = 0
        
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]-1:
                maxi = maxi + 1
                mx = max(maxi,mx)
            elif nums[i] == nums[i+1]:
                pass
            else:
                maxi = 0
                
        return mx+1