class Solution:
    def countOrders(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        return self.countOrders(n-1)*(2*n-1)*n%(10**9 + 7)
        