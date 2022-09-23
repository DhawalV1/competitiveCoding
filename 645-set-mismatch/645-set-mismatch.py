class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        sumu = 0
        d = {}
        for i in nums:
            sumu += i
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        p = (len(nums)*(len(nums)+1))//2 - sumu
        
        for key in d.keys():
            if d[key]==2:
                return [key,key+p]
        
        