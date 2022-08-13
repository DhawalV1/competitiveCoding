class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        sumi = 0
        for i in range(len(edges)):
            sumi = sumi + sum(edges[i])
        return (sumi - (n+1)*(n+2)//2)//(n-1)