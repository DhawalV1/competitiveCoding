class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        
        maxi = float('-inf')
        l = 0
        for i in gain:
            
            l = l + i
            maxi = max(maxi,l)
            
        return maxi if maxi>=0 else 0