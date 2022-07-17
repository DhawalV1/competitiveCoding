class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i = j = 0
        maxi = 0
      
        k=0
        while j<len(nums2):
            while i<len(nums1) and nums1[i]>nums2[j]:
                i+=1
            if (i<len(nums1)):
                maxi=max(maxi,j-i)
            j+=1
            if i==len(nums1):
                break
        return maxi
            