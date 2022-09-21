class Solution:
    def threeSumClosest(self, nums: List[int], x: int) -> int:
        nums.sort()
        closest = sys.maxsize
        for i in range(len(nums)-2):
            p = i+1
            q = len(nums)-1
            while p<q:
                
                sum1 = nums[p] + nums[q] + nums[i] 
                if (abs(x-sum1) < abs(x-closest)):
                    closest = sum1
                    
                if sum1 > x:
                    q-=1
                else:
                    p+=1
        return closest