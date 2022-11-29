class Solution:
    def isGoodArray(self, nums: List[int]) -> bool:
        return True if reduce(gcd, nums) == 1 else False
        