class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        if len(nums2) > len(nums1):
            return self.findLength(nums2,nums1)
        m = len(nums1)
        n = len(nums2)
        dp,prev = [0]*(n+1),[0]*(n+1)
        ans = 0
        for i in range(1,m+1):
            for j in range(1,n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[j] = prev[j-1] + 1
                else:
                    dp[j] = 0
                    
                ans = max(ans,dp[j])
            prev,dp = dp,prev
            
        return ans
        