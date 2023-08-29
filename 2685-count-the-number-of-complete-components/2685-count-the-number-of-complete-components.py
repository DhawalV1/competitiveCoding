class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        dictt = {}
        
        for i,j in edges:
            if i in dictt:
                
                dictt[i].append(j)
            else:
                
                dictt[i] = [j]
            if j in dictt:
                
                dictt[j].append(i)
            else:
                
                dictt[j] = [i]
        print(dictt)
        '''
        g = defaultdict(list)
        
        for i,j in edges:
            g[i].append(j)
            g[j].append(i)
            
        def dfs(i):
            comp.add(i)
            for adj in g[i]:
                if adj not in visited:
                    visited.add(adj)
                    dfs(adj)
        res = 0
        visited = set()
        for i in range(n):
            if i not in visited:
                visited.add(i)
                comp = set()
                dfs(i)
                if all(len(g[node]) == len(comp) - 1 for node in comp):
                    res += 1
        return res
                
            
        