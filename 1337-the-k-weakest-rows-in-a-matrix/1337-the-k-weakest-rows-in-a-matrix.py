class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        count = []
        for i in range(len(mat)):
            count.append([mat[i],i])
    
        
        return [j for i,j in sorted(count)[0:k]]
  
            
        