class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        sumi = sum(beans)
        arr = []
        for i in range(len(beans)):
            arr.append(sumi-(len(beans)-i)*beans[i])
        return min(arr)
            
        
        
        
        
