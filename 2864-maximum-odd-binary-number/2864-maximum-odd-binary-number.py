class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zero = s.count('0')
        one = len(s)-zero
        return zero*'0'+'1' if one==1 else (one-1)*'1'+zero*'0'+'1'
        