class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        if [source, destination] in edges:
            return True
        
        if edges == 0:
            return False
        
        graph = defaultdict(list)
        
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
        
        visited = set()
        
        def dfs(node):
            if node == destination:
                return True
            
            visited.add(node)
            
            for child in graph[node]:
                if child not in visited and dfs(child):
                    return True
                
            return False
          
        return dfs(source)