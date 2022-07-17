class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        sum = (k+1)*k//2
        level = k+1
        s = sorted(set(nums))
        for x in s:
            if x<level:
                sum += level - x
                level += 1
        return sum
        
        
        
        
        
            
        