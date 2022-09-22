class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        q = deque([start])
        while q:
            cur = q.popleft()
            if arr[cur] == 0:
                return True
            if arr[cur] <0: 
                continue
            if cur + arr[cur] < len(arr):
                q.append(cur + arr[cur])
            if cur - arr[cur] >= 0:
                q.append(cur-arr[cur])
            arr[cur] *= -1
            
        return False
                
            
            
        