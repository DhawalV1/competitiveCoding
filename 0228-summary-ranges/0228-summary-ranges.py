class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        out = []
        
        n = len(nums)
        if n==0: return []
        if n==1: return ["{}".format(nums[0])]
        nums.append(float('inf'))
        i = 0
        j = 1
        while i<n+1 and j<n+1:
            if nums[j] == nums[j-1] + 1:
                
                j += 1
                
            else:
                if i != j-1:
                    p = "{}->{}".format(nums[i],nums[j-1])
                    out.append(p)
                    i = j+1
                else:
                    q = "{}".format(nums[i])
                    out.append(q)
                i = j
                j += 1
        
            
        return out
        