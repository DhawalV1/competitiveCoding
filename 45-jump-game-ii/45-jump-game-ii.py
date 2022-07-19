class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1: return 0
        l, r = 0, nums[0]
        times = 1
        while r < len(nums) - 1:
            times += 1
            nxt = max(i + nums[i] for i in range(l, r + 1))
            l, r = r, nxt
        return times
            
    '''
    def helper(self,nums,i):
        return nums[i]
    '''
    
    '''
        
        dp = [10001]*len(nums)
        return self.solve(nums,dp,0)
    
    def solve(self,nums,dp,pos):
        if pos >= len(nums)-1:
            return 0
        if dp[pos]!=10001:
            return dp[pos]
        for i in range(1,nums[pos],1):
            dp[pos] = min(dp[pos],1+self.solve(nums,dp,pos+i))
        return dp[pos]
        
            
    '''
        