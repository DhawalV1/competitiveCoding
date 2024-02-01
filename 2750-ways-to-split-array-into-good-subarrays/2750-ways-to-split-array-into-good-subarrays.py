class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        if sum(nums)<2:return sum(nums)
        
        mod = 10**9+7
        pro = 1
        
        ind = nums.index(1)
        for i in range(ind+1,len(nums)):
            if nums[i]==1:
                pro = pro*(i-ind)%mod
                ind = i
        return pro
                
        