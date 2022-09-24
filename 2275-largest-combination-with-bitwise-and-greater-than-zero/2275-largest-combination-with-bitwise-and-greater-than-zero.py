class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        maxi = 0
        for i in range(25):
            count = 0
            for a in candidates:
                if (1 << i & a) > 0:
                    count += 1
                    
            maxi = max(maxi,count)
            
        return maxi
                    
                
        