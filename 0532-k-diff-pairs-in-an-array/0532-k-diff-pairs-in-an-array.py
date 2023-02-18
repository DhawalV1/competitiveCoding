class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k == 0:
            v = collections.Counter(nums)
            count = 0
            for key in v.keys():
                if v[key]>1:
                    count += 1
            return count
        seen = set(nums)
        count =  0
        for i in seen:
            
            if i + k in seen:
                
                count += 1
                
        return count