class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)
        res = float('inf')
        
        def dfs(node,arr,count=0):
            
            while arr[node]==-1  and node!=-1:
                
                arr[node] = count
                dfs(edges[node],arr,count+1)
                
            return arr
        
        arr1 = [-1 for i in range(n)]
        dfs(node1,arr1)
        
        arr2 = [-1 for i in range(n)]
        dfs(node2,arr2)
        
        ans = -1
        
        for i in range(n):
            
            if arr1[i]!=-1 and arr2[i]!=-1:
                
                ansi = max(arr1[i],arr2[i])
                
                if ansi<res:
                    res = ansi
                    ans = i
                    
        return ans
                