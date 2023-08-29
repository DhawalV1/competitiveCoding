class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        nb = []
        for i in nums:
            if i!=0:
                nb.append(i)
        if len(nb) == 0:
            return 0
        if len(nb) == 1:
            if nb == nums: return nb[0]
            elif nb[0]<0: return 0
            
            else:
                return nb[0]
        prod1 = 1
        maxi = -1
        
        for i in nb:
            prod1 *= i
        if prod1>0:
            return prod1
        for i in nb:
            maxi = max(maxi,prod1//i)
            
        return maxi
        