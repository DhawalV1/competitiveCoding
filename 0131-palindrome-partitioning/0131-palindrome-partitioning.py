class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
       
        ret = []
        self.dfs(s, [], ret)
        return ret
    
    def dfs(self, nums, path, ret):
        if not nums:
            ret.append(path)
            
        for i in range(1,len(nums)+1):
            if self.ispal(nums[:i]):
                self.dfs(nums[i:], path+[nums[:i]], ret)
                
    def ispal(self,nums):
        return nums == nums[::-1]
        