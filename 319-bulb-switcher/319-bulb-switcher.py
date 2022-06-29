class Solution:
    def bulbSwitch(self, n: int) -> int:
        i = 0
        while i * i <= n:
            i = i + 1
            
        return i-1
            