class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        ans = [0,0]
        for i in range(len(nums)):
            val = abs(nums[i])
            ans[1] ^= (i+1)^val
            if nums[val-1] < 0: ans[0] = val
            else: nums[val-1] = -nums[val-1]
            
        ans[1]^=ans[0]
        return ans
        
        # sum of number and sum of squares
        
        
        ''''
        
        sumu = 0
        d = {}
        for i in nums:
            sumu += i
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        p = (len(nums)*(len(nums)+1))//2 - sumu
        
        for key in d.keys():
            if d[key]==2:
                return [key,key+p]
            
        '''
        '''    
        missing_num = sum( range( len(nums)+1) ) - sum( set(nums) )
        
       
        dup = sum(nums) - sum(set(nums))


        
        return dup,missing_num
        '''        
        
        