class Solution:
    def finalPrices(self, A: List[int]) -> List[int]:
        i = 0
        j = i + 1
        while i < j and j < len(A):
            if A[i]>=A[j]:
                A[i] = A[i]-A[j]
                i = i+1
                j = i+1
                
            else:
                if (j == len(A)-1):
                    i = i+1
                    j = i+1
                else:
                    j=j+1
        return A
        