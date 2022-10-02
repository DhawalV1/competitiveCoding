class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)
        if m%2==0 and n%2==0:
            return 0
        if n%2==0 and m%2==1:
            return reduce(operator.xor,nums2)
        if n%2==1 and m%2==0:
            return reduce(operator.xor,nums1)
        else:
            return reduce(operator.xor,nums1)^reduce(operator.xor,nums2)
            
            
            
        