class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        dp = []
        for i in range(len(nums),0,-1):
            for j in range(i-1):
                if not self.give(nums[j],nums[j+1]):
                    nums[j],nums[j+1] = nums[j+1],nums[j]
                    
        return str(int(''.join(map(str,nums))))
        
                
                    
        
                    
        
    def give(self,m,n):
        return str(m)+str(n)>str(n)+str(m)
        