class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        uf = {}
        def find(x):
            if x!=uf[x]:
                uf[x] = find(uf[x])
            return uf[x]
            
        def union(x,y):
            
            uf.setdefault(x,x)
            uf.setdefault(y,y)
            uf[find(x)] = find(y)
            
        for i,j in stones:
            union(i,~j)
        return len(stones) - len({find(x) for x in uf})
        