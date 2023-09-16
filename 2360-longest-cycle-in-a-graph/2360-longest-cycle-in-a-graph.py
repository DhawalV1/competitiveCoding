class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        '''
        #seen1 = set()
        #if cycle(edge,x)==False:
        seenloop = set()
        nonloop = set()
            
        #for i in range(len(edges)):
            #start = i
        dist = [0]*len(edges)
            
        def cycle(edges,x):
            y = x
            vis = False
            seen = set()
            count = 0

            while vis == False:
                seen.add(x)
                count += 1
                #seenloop.add(x)
                #nonloop.add(x)
                x = edges[x]
                if x in seen:
                    vis = True


            if y == x:
                if edges[x]!=-1:
                    seenloop.add(y)
                    dist[y] = count
                
            else:
                nonloop.add(y)
                
            
        for i in range(len(edges)):
            if i not in seenloop or nonloop:
                cycle(edges,i)
            
        print(seenloop,nonloop,dist)
        if max(dist)==0 or len(seenloop)<2:return -1
        return max(dist)
        #return max(dist)
        
        '''
        n = len(edges)
        self.max_length = float('-inf')
        seen = [False] * n
        visiting = {}
        stack = []

        def dfs(node):
            if not seen[node]:
                if node in visiting:
                    self.max_length = max(self.max_length, len(stack) - visiting[node])
                elif edges[node] != -1: 
                    visiting[node] = len(stack) 
                    stack.append(node)
                    dfs(edges[node])
                    stack.pop()
                    visiting.pop(node)
                seen[node] = True

        for i in range(n):            
            dfs(i)
        return self.max_length if self.max_length > 0 else -1  
                
        