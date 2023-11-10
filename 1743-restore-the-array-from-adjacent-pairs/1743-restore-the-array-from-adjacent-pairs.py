class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = collections.defaultdict(list)
        for num in adjacentPairs:
            graph[num[0]].append(num[1])
            graph[num[1]].append(num[0])
        print(graph)
        
        seen = set()
        
        stack = collections.deque()
        for node in graph:
            if len(graph[node])==1:
                stack.append(node)
                break
        ans = []
        
        while stack:
            node = stack.popleft()
            ans.append(node)
            seen.add(node)
            for ele in graph[node]:
                if ele not in seen:
                    stack.append(ele)
        return ans
                    