class Solution:
    def rob(self, nums: List[int]) -> int:
        last,now = 0,0
        for i in nums:
            last,now = now,max(i+last,now)
            
        return now
            