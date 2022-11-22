class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        out = []
        nums1.sort()
        nums2.sort()
        nums1 = list(set(nums1))
        nums2 = list(set(nums2))
        
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j]:
                    out.append(i)
                    
        return set(out)
            
        