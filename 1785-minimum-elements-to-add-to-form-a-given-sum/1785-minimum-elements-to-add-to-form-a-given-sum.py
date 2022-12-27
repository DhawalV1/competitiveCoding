class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        
        p = goal - sum(nums)
        
        if p == 0: return 0
        
        if p > 0: return (p-1)//limit + 1
        
        if p < 0: return (-p-1)//limit + 1