class Solution:
    def letterCombinations(self, nums: str) -> List[str]:
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        if len(nums) == 0:
            return []
        if len(nums) == 1:
            return list(mapping[nums[0]])
        prev = self.letterCombinations(nums[:-1])
        additional = mapping[nums[-1]]
        return [s+c for s in prev for c in additional]