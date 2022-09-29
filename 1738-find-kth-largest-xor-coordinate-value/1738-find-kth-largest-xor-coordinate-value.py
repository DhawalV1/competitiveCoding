class Solution:
    def kthLargestValue(self, m: List[List[int]], k: int) -> int:
        
        l = len(m)
        n = len(m[0])
        pq = []
        for i in range(l):
            for j in range(n):
                if i: m[i][j] ^= m[i-1][j]
                if j: m[i][j] ^= m[i][j-1]
                if i and j: m[i][j] ^= m[i-1][j-1]
                    
                if len(pq) < k:
                    heappush(pq,m[i][j])
                    
                else:
                    heappushpop(pq,m[i][j])
                    
        return pq[0]
        
        