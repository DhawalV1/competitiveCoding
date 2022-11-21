class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        
        n = len(nums1)
        
        swap,nswap = [n]*n,[n]*n
        
        swap[0] = 1
        nswap[0] = 0
        
        for i in range(1,n):
            if nums1[i-1]<nums1[i] and nums2[i-1]<nums2[i]:
                swap[i] = swap[i-1] + 1
                nswap[i] = nswap[i-1]
                
            if nums1[i-1]<nums2[i] and nums2[i-1]<nums1[i]:
                swap[i] = min(swap[i],nswap[i-1]+1)
                nswap[i] = min(swap[i-1],nswap[i])
                
        return min(swap[-1],nswap[-1])
        