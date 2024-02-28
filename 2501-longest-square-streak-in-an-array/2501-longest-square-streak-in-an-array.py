class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        square = {}
        res = -1
        for i in sorted(nums,reverse=True):
            if i*i in square:
                square[i] = square[i*i]+1
                res = max(res,square[i])
            else:
                square[i] = 1
                
        return res
                
        
                
        