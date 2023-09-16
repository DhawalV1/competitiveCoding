class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        count = [0]*1001
        dicti = {}
        for i in range(len(nums)-1):
            if nums[i]==key:
                count[nums[i+1]]+= 1
                
        return count.index(max(count))
        