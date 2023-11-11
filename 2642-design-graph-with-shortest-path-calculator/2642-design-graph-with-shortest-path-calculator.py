class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(dict)
        for a,b,cost in edges:
            self.graph[a][b] = cost

    def addEdge(self, edge: List[int]) -> None:
        
        self.graph[edge[0]][edge[1]] = edge[2]
        
        

    def shortestPath(self, node1: int, node2: int) -> int:
        
        g = self.graph
        seen = set()
        heap = [(0,node1)]
        while heap:
            cost,node = heappop(heap)
            if node == node2:
                return cost
            if node not in seen and node in g:
                seen.add(node)
                for kid,cost1 in g[node].items():
                    heappush(heap,(cost+cost1,kid))
                             
        return -1
        


# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)