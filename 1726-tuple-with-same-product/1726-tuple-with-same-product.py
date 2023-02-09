class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        seen = defaultdict(int)
        ans = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                k = nums[i]*nums[j]
                ans += seen[k]
                seen[k] += 1
                
                
        return ans*8
        