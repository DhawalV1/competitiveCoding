class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        m =len(nums)
        nums.reverse()
        for i in range(k):
            nums.append(nums.pop(0))
        return nums.reverse()
    
        
        """
        Do not return anything, modify nums in-place instead.
        """
        