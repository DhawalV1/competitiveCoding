class Solution:
    def maxProfit(self, inv: List[int], orders: int) -> int:
        inv.sort(reverse=True)
        inv.append(0)
        ans, ind, width=0,0,0
        
        while orders>0:
            width += 1
            sell=min(orders, width * (inv[ind] - inv[ind+1]))
            whole, remainder= divmod(sell, width)
            ans += width*(whole*(inv[ind]+inv[ind]-(whole-1)))//2 + remainder*(inv[ind]-whole)
            orders -= sell
            ind += 1
        return ans % 1_000_000_007      