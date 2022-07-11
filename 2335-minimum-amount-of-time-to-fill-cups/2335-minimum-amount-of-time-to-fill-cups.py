class Solution:
    def fillCups(self, amount: List[int]) -> int:
        amount.sort()
        return max(amount[2], (sum(amount) + 1) // 2)
            
        