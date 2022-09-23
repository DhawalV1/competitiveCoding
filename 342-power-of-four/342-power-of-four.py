class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<0:
            return False
        else:
            return bin(n)[2:].count('0')%2==0 and bin(n)[2:].count('0')==len(bin(n))-3
        
        