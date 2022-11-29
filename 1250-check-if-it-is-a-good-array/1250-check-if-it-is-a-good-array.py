class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        if nums == [1]:return True
        if len(nums)==1:return False
        k = self.gcde(nums[0],nums[1])
        if k == 1:return True
        for i in range(2,len(nums)):
            k = self.gcde(k,nums[i])
            if k == 1:return True
        return False
            
    def gcde(self,m,n):
        if m>=n:
            if m%n==0:return n
            return self.gcde(m%n,n)
        elif m<n:
            if n%m==0:return m
            return self.gcde(n%m,m)
        