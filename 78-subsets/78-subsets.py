class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        def dfs(num,path):
            res.append(path)

            for i in range(len(num)):
                dfs(num[i+1:],path+[num[i]])
        dfs(nums,[])
       
        return res
   
        
        
        #res = [[]]
        #for i in nums:
            #res += [item + [i] for item in res]
        #return res        
        
        
        
        