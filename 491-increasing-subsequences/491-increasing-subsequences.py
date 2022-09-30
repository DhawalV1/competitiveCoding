class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def dfs(self,start,path):
            if len(path)>=2:
                res.append(path)
                
            used = set()
            for i in range(start,len(nums)):
                if not path or path[-1]<=nums[i]:
                    if nums[i] not in used:
                        used.add(nums[i])
                        dfs(self,i+1,path+[nums[i]])
                        
        dfs(self,0,[])
        return res
                    
        