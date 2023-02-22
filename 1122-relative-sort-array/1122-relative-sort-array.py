class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        seen = set(arr2)
        cou = collections.Counter(arr1)
        res = []
        addi = []
        for i in arr2:
            
            res += [i]*cou[i]
                
        for i in arr1:
            
            if i not in seen:
                
                addi.append(i)
                
        return res + sorted(addi)