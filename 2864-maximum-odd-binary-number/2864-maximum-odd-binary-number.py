class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        
        return collections.Counter(s)['0']*'0'+'1' if collections.Counter(s)['1']==1 else (collections.Counter(s)['1']-1)*'1'+collections.Counter(s)['0']*'0'+'1'
        