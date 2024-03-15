class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = []
        prefix = 1
        for i in range(len(nums)):
            pre.append(prefix)
            prefix = prefix * nums[i]
        pref = 1
        for i in range(len(nums)-1,-1,-1):
            pre[i] = pre[i] * pref
            pref = pref * nums[i]
        return pre
            
        