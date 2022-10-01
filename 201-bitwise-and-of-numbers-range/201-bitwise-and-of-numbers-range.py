class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        
        andi = right
        while andi > left:
            andi = andi & (andi-1)
            
            
        return andi
            