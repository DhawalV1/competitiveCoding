class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        
        ans = 0
        sum1,sum2 = sum(nums1),sum(nums2)
        
        ans = max(sum1,sum2)
        
        f,s,max1,max2 = 0,0,0,0
        
        for i in range(len(nums1)):
            f += nums2[i]-nums1[i]
            s += nums1[i]-nums2[i]
            
            max1 = max(max1,f)
            max2 = max(max2,s)
            
            if f <0: f = 0
            if s<0: s = 0
                
        ans = max(ans,sum1+max1,sum2+max2)
     
            
        return ans
        
        
        