class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        lst = set()
        n = len(nums)
        for i in range(n-2):
            start = i+1
            end = n-1
            while(start<end):
                if(nums[i]+nums[start]+nums[end]==0):
                    lst.add((nums[i],nums[start],nums[end]))
                    end-=1
                elif(nums[i]+nums[start]+nums[end]>0):
                    end-=1
                else:
                    start+=1
        return list(lst)