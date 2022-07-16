class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        self.dfs(nums,[],ret)
        return ret
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return # backtracking
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)