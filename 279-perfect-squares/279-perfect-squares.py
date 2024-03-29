class Solution:
    def numSquares(self, n: int) -> int:
        if n <= 0:
            return 0
        arr = [float('inf')]*(n+1)
        arr[0] = 0
        for i in range(1,n+1):
            j = 1
            while j*j <= i:
                arr[i] = min(arr[i],arr[i-j*j]+1)
                j = j+1
        return arr[-1]
        