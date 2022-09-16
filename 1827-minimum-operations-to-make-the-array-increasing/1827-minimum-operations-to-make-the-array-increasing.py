class Solution:
    def minOperations(self, nums: List[int]) -> int:
        now = nums[0]
        nops = 0
        i = 1
        while i < len(nums):
            if nums[i]<now:
                nops += now-nums[i]+1
                nums[i] = now+1
                now = nums[i]
            elif nums[i]==now:
                nops += 1
                nums[i] = now + 1
                now = nums[i]
            else:
                now = nums[i]
            i += 1
            
        return nops
                
            
        