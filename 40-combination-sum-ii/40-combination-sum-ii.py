class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        self.dfs(sorted(candidates),target,0,[],ret)
        return ret
    
    def dfs(self,arr,target,idx,path,ret):
        if target <= 0:
            if target == 0:
                ret.append(path)
            return 
        
        for i in range(idx,len(arr)):
            if i > idx and arr[i] == arr[i-1]:
                continue
            self.dfs(arr,target - arr[i],i+1,path + [arr[i]],ret)