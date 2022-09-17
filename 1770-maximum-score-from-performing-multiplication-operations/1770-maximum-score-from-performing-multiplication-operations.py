class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        
        n = len(nums)
        m = len(multipliers)
        
        dp = [0]*(m+1)
        
        for i in range(m-1,-1,-1):
            
            nexti = dp.copy()
            
            for left in range(i,-1,-1):
                
                dp[left] = max(nexti[left+1] + nums[left]*multipliers[i],nexti[left]+nums[n-1-(i-left)]*multipliers[i])
        
        
        return dp[0]