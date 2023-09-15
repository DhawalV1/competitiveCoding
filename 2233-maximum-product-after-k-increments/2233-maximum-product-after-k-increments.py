class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        mod = 10**9+7
        heap = []
        for i in nums:
            heapq.heappush(heap,i)
            

            
        while k:
            cur = heapq.heappop(heap)
            heapq.heappush(heap,cur+1)
            k -= 1
            
        res = 1
        while len(heap):
            x = heapq.heappop(heap)
            res = res*x%mod
            
        return res
      
        
        
        
        
        
        
        