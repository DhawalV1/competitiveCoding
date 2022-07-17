class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        res = 0
        cur = 1
        nums.append(float('inf'))
        nums.sort()
        for i in range(len(nums)):
            take = max(0,min(k,nums[i]-cur))
            res += (cur+take)*(cur + take - 1)/2 - cur*(cur-1)/2
            k -= take
            cur = nums[i]+1
        return int(res)
        
        
        
        
        
        
            
        