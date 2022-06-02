class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:   
        start = 1
        for x in nums[1:]:
            if x != nums[start - 1]:
                nums[start] = x
                start += 1
        return start