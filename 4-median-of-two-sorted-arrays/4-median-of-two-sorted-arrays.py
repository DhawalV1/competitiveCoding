class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m =  len(nums1)
        n = len(nums2)
        
        if m>n:
            return self.findMedianSortedArrays(nums2,nums1)
        start = 0
        end = m
        realmid = (m+n+1)//2
        
        while start<=end:
            mid = (start+end)//2
            leftas = mid
            leftbs = realmid - mid
            
            lefta = nums1[leftas-1] if leftas>0 else float('-inf')
            leftb = nums2[leftbs-1] if leftbs>0 else float('-inf')
            righta = nums1[leftas] if m>leftas else float('inf')
            rightb = nums2[leftbs] if n>leftbs else float('inf')
            
            if lefta <= rightb and leftb <= righta:
                if (m+n)%2==0:
                    return (max(lefta,leftb)+min(righta,rightb))/2.0
                return max(lefta,leftb)
            elif lefta>leftb:
                end = mid - 1
            else:
                start = mid + 1
         
        
    
        
            
            
        
        
        
        
            