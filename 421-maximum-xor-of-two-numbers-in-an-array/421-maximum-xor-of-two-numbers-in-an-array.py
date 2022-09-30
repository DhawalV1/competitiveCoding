class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        ans = 0
        mask = 0
        n = len(bin(max(nums))[2:])+1
        for i in range(n,-1,-1):
            mask|= 1<<i
            
            found = set([num & mask for num in nums])
            
            start = ans|1<<i
            
            for pref in found:
                if start^pref in found:
                    ans = start
                    break
                    
        return ans
        
        
        
        
       