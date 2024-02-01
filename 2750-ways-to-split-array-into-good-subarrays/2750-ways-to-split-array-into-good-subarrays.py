class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        if sum(nums)==1:return 1
        if sum(nums)==0:return 0
        mod = 10**9+7
        pro = 1
        
        ind = nums.index(1)
        for i in range(ind+1,len(nums)):
            if nums[i]==1:
                pro = pro*(i-ind)%mod
                ind = i
        return pro
                
        