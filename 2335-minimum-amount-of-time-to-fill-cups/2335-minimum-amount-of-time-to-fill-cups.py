class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        res = 0
        while amount[2] > 0:
            
            
            amount[2] -= 1
            res += 1
            if amount[1] > 0:
                amount[1] -= 1
            amount.sort()
            
                
        return res
                
            
        