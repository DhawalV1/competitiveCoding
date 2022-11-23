class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        
        mapi = {}
        maxi = -1
        for i in nums:
            if -i in mapi:
                mapi[i] = 0
                maxi = max(maxi,abs(i))
            else:
                mapi[i] = 1
                
        return maxi