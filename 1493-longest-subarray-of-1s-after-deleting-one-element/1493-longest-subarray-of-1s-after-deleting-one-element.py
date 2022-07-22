class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if sum(nums) == len(nums):
            return len(nums)-1
        maxi = 0
        smaxi = 0
        count1 = 0
        nums.append(0)
        nums.append(1)
        c = []
        d = []
        for i in range(len(nums)):
            if nums[i] == 1:
                count1 += 1
            else:
                c.append(count1)
                count1 = 0
                if nums[i+1]==0:
                    c.append(0)
                    d.append(c)
                    c = []
        d.append(c)
        if len(d[0])==1:
            return d[0][0]
        for i in range(len(d)):
            maxi = 0
            for j in range(len(d[i])-1):
                maxi = max(maxi,d[i][j]+d[i][j+1])
            smaxi = max(smaxi,maxi)
            
        return smaxi
                
                
            
                
                
            
        