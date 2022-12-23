class Solution:
    def maxProfit(self, p: List[int]) -> int:
        
        if len(p)<=1: return 0
        
        hold, buy, sell = 0,-p[0],float('-inf')
        
        maxi = buy
        
        for i in range(1, len(p)):
            temp = hold
            hold = max(hold,buy,sell)
            buy = temp - p[i]
            sell = p[i] + maxi
            
            maxi = max(maxi,buy)
            
        return max(hold,buy,sell)