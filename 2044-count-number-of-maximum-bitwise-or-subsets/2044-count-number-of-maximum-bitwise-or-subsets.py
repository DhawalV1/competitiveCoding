class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        a = 0
        for i in  nums:
            a = a|i
            
        return self.subset(nums,len(nums)-1,a,0)
        
    def subset(self,arr,i,a,b):
        
        ans = 0
        if i < 0:
            return 0
        if a == b|arr[i]:
            ans = 1
            
        return ans + self.subset(arr,i-1,a,b) + self.subset(arr,i-1,a,b|arr[i])