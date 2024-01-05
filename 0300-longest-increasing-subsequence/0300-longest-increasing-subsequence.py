class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        k =len(nums)
        p = [0]*(k+1)
        n = 1
        p[0] = nums[0]
        for i in range(1,k):
            if nums[i] < p[0]:
                p[0] = nums[i]
            elif nums[i] > p[n-1]:
                p[n] = nums[i]
                n+=1
            else:
                p[self.helper(p,-1,n-1,nums[i])] = nums[i]
        
        return n

        
    def helper(self,arr,l,r,key):
        while r-l > 1:
            m = (l+r)//2
            if arr[m]>=key:
                r = m
            else:
                l = m
        return r
        
       