class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums,[],res)
        return res
    def dfs(self,num,path,res):
        res.append(path)
        
        for i in range(len(num)):
            self.dfs(num[i+1:],path+[num[i]],res)
            
        