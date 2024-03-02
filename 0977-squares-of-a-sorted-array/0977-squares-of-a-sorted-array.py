class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l=0
        out = [0]*len(nums)
        r= len(nums) -1
        k = len(nums)-1
        while l<= r:
            if(nums[l]**2) > (nums[r]**2):
                out[k] = nums[l]**2
                l += 1
                k -= 1
            else:
                out[k] = nums[r]**2
                k -= 1
                r -= 1
        return out
                
            
            
        