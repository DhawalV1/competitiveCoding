class Solution:
    def largestSumOfAverages(self, nums: List[int], K: int) -> float:
        memo = {}
        def search(n,k):
            if (n,k) in memo:
                return memo[n,k]
            if n<k: return 0
            if k == 1:
                memo[n,k] = sum(nums[:n])/float(n)
                return memo[n,k]
            cur, memo[n,k] = 0,0
            for i in range(n-1,0,-1):
                cur += nums[i]
                memo[n,k] = max(memo[n,k],search(i,k-1)+cur/float(n-i))
            return memo[n,k]
        return search(len(nums),K)
        
        
       