class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        
        costs.sort()
        count = 0
        for i in costs:
            coins -= i
            count += 1
            if coins<0:
                return count-1
        
        if coins>=0: return len(costs)