class Solution:
    def getMoneyAmount(self, n: int) -> int:
        cache = [[float('inf')]*(n+1) for _ in range(n+1)]
        return self.cost(1,n,cache)
    
    def cost(self,lo,hi,cache):
        if lo>=hi:
            return 0
        if cache[lo][hi] != float('inf'):
            return cache[lo][hi]
        for k in range(lo,hi+1):
            cache[lo][hi] = min(cache[lo][hi],max(self.cost(lo,k-1,cache),self.cost(k+1,hi,cache))+k)
        return cache[lo][hi]
        
        
        
        
        
         
        