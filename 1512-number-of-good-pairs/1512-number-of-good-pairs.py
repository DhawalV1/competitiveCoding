class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        sumi = 0
        x = collections.Counter(nums)
        print(x)
        
        for key in x.keys():
            if x[key]>1:
                sumi += (x[key]-1)*x[key]//2
        return sumi