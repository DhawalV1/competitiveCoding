class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ''''
        maxi = max(nums)
        res = 1
        count = 0
        for n in nums:
            if n == maxi:
                count += 1
                
            else:
                count = 0
                
                
            res = max(res,count)
            
        return res
        
        '''
        mx = 0
        lng = 0
        cur = 0
        for num in nums:
            if num > mx:
                mx = num
                lng = 1
                cur = 1
            elif num == mx:
                cur += 1
                lng = max(lng,cur)
                
            else:
                cur = 0
                
        return lng