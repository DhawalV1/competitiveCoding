class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        return chr(reduce(operator.xor,[ord(i) for i in list(s+t)]))
        