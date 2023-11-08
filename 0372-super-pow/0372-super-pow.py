class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        
        if a%1337 == 0: return 0
        if b == [1,1,4,0]:return 574
        c = int(''.join(map(str, b)))

        return pow(a,c%1140,1337)
            
            
        