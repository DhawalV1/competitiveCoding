class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:
        mod = 10**9+7
        k = target // 2
        if n <= k:
            return (n * (n + 1) // 2)%mod
        return (k * (k + 1) // 2 % mod + (target + target + n - k - 1) * (n - k) // 2 % mod)%mod