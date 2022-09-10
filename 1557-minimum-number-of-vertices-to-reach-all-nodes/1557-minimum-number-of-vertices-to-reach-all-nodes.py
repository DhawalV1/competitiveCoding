class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        a = []
        d = {}
        for j in range(len(edges)):
            if edges[j][1] not in d:
                d[edges[j][1]] = edges[j][1]
        for i in range(n):
            if d.get(i) is None:
                a.append(i)
            
        return a
