class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s1 = -prices[0]
        s2,s3,s4 = float('-inf'), float('-inf'), float('-inf')
        for i in prices:
            s1 = max(s1,-i)
            s2 = max(s2,s1+i)
            s3 = max(s3,s2-i)
            s4 = max(s4,s3+i)
            
        return max(0,s4)
            
        