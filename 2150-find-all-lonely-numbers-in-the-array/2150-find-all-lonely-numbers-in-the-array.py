class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        nums = [-4]+nums+[1000002]
    
        nums.sort()
        res = []
        for i in range(1,len(nums)-1):
            if nums[i]!=nums[i-1]+1 and nums[i]!=nums[i+1]-1:
                res.append(nums[i])
        if nums[0]!=nums[1]-1:
            res.append(nums[0])
        if nums[-1]!=nums[-2]+1:
            res.append(nums[-1])
        count = collections.Counter(nums)
        res1 = []
        for i in res:
            if count[i]>1:
                continue
            else:
                res1.append(i)
        return res1[:len(res1)-2]