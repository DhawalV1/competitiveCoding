class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for i,v in enumerate(nums):
            if v in d:
                if abs(i-d[v])<=k:
                    return True
                else:
                    d[v] = i
                
            else:
                d[v] = i
                
        return False