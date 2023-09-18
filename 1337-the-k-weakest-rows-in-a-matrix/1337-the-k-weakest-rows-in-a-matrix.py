class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        count = []
        for i in range(len(mat)):
            count.append([sum(mat[i]),i])
        ans = []
        #or i,j in sorted(count):
            #ns.append(j)
        return [j for i,j in sorted(count)[0:k]]
        #rint(sorted(count))
            
        