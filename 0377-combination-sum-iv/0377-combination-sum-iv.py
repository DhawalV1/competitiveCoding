class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        ans = [-1]*(target+1)
        return self.comb(nums,target,ans)
        
    def comb(self,nums,target,ans):
        if target == 0: return 1
        if target < 0: return 0
        if ans[target]!= -1: return ans[target]
        ans[target]=0
        
        for i in range(len(nums)):
            if nums[i]<= target:
                ans[target] += self.comb(nums,target-nums[i],ans)
        return ans[target] 
      
        