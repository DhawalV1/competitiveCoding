class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        dp = collections.defaultdict(int)
        for num in arr:
            dp[num] = max(dp[num], 1+dp[num-d])
        return max(dp.values())
            
            
        