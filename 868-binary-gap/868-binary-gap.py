class Solution:
    def binaryGap(self, n: int) -> int:
        bits=bin(n)
        bits=bits[2:]
        ans=0
        i=0
        j=0
        while j<len(bits):
            if bits[j]=="1":
                if (j-i)>ans:
                    ans=j-i
                i=j
            j=j+1
        return ans
        