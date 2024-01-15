class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        n = len(arr)
        
        for i in range(n,0,-1):
            ind = arr.index(i)
            if ind == i-1:
                continue
            if ind!=0:
                res.append(ind+1)
                arr[:ind+1] = arr[:ind+1][::-1]
            res.append(i)
            arr[:i] = arr[:i][::-1]
            
        return res
                
                
                