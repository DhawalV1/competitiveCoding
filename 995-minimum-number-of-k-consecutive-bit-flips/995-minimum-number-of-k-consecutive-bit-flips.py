class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        fliped = 0
        ans = 0
        n = len(nums)
        
        for i in range(n):
            if i >= k and nums[i-k]>1:
                fliped -= 1
                nums[i-k] -= 2  
            if fliped%2 == nums[i]: 
                if i + k > n:
                    return -1
                ans += 1
                fliped += 1
                nums[i] += 2
        
        return ans