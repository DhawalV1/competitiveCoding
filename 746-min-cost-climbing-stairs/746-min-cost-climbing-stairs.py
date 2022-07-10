class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        dp = [0]*len(cost)
        
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2,len(cost)):
            cost[i] = cost[i] + min(cost[i-1],cost[i-2])
            
        return min(cost[-1],cost[-2])
        
        