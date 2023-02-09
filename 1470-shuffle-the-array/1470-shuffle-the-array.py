class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        for i in range(n, 2*n):
            nums[i] = (nums[i] << 10) | nums[i-n]
        
        for i in range(n, 2*n):
            nums[(i-n)*2] = nums[i] & (2 ** 10 - 1)
            nums[(i-n)*2+1] = nums[i] >> 10
        
        return nums