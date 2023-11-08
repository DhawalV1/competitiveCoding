class Solution:
    def monkeyMove(self, n: int) -> int:
        if pow(2,n,1000000007)==1:return 1000000006
        return pow(2,n,1000000007)-2
        