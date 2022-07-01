class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        ma = nums[0]
        mi = nums[0]
        ans = nums[0]
        
        for i in range(1,len(nums)):
            
            if nums[i] < 0:
                ma,mi = mi,ma
            ma = max(nums[i],nums[i]*ma)
            mi = min(nums[i],nums[i]*mi)
            
            if ans < ma:
                ans = ma
                
        return ans
        
        
        
        