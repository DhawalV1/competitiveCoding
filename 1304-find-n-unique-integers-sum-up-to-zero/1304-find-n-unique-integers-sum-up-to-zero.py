class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n%2==0:
            return [i for i in range(-(n-1)//2,n//2+1) if i!=0]
        else:
            return [i for i in range(-(n-1)//2,(n+1)//2)]