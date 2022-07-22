class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        i = 0
        count = 0
        res = 0
        while i<len(nums)-2:
                if 2*nums[i+1] == (nums[i]+nums[i+2]):
                        count = count+1
                        i = i+1
                else:
                        res = res + count*(count+1)//2
                        count = 0
                        i = i+1
                print(i,count)
        res = res + count*(count+1)//2
        return res
        