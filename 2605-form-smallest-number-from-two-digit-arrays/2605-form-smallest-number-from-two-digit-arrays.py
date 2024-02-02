class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        mini = float('inf')
        for i in sorted(nums1):
            if i in nums2:
                mini = min(mini,i)
        if mini!=float('inf'):
            return mini
        p = min(nums1)
        q = min(nums2)
        
        return int(str(min(p,q))+str(max(p,q)))
                
        