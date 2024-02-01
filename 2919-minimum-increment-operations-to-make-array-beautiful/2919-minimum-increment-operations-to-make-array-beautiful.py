class Solution:
    def minIncrementOperations(self, A: List[int], k: int) -> int:
        dp1, dp2, dp3 = 0,0,0
        for a in A:
            dp1, dp2, dp3 = dp2, dp3, min(dp1, dp2, dp3) + max(k - a, 0)
        return min(dp1, dp2, dp3)