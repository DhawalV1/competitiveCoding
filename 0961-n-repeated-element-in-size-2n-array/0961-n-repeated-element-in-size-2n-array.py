class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = collections.Counter(nums)
        for key in count.keys():
            if count[key]>1:
                return key
        
        