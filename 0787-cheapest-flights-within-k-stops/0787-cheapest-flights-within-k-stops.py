class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        vis = {}
        graph = collections.defaultdict(list)
        for i in flights:
            graph[i[0]].append((i[1],i[2]))
            
        heap = [(0,0,src)]
        
        while heap:
            dist,move,nodes = heapq.heappop(heap)
            
            if nodes == dst and k>=move-1:
                return dist
            if nodes not in vis or vis[nodes] > move:
                vis[nodes] = move
                for n,w in graph[nodes]:
                    heapq.heappush(heap,(dist + w, move + 1,n))
                    
        return -1