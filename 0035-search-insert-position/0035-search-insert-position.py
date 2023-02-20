class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low = 1 
        high = max(nums)
        ans = max(nums)
        
        if target in nums:
            
            while low <= high:
                
                mid = (high + low) // 2
                
                if mid == target:
                    ans = nums.index(mid) #nums[mid]
                    break
                    
                elif target < mid:
                    high = mid - 1
                    
                elif target > mid:
                    low = mid + 1
        else:   
            nums.append(target)
            nums.sort()
            ans = nums.index(target)   
            
        return ans 
                
            
        