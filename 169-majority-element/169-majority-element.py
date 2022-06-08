class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        return max(Counter(nums), key=count.get)
        