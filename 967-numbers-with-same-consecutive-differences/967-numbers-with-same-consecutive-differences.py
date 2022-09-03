class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        
        numset = range(1,10)
        for i in range(n - 1):
            res = []
            for num in numset:
                cur = num % 10

                if cur + k <= 9: res.append(num * 10 + cur + k)
                if k != 0 and cur - k >= 0: res.append(num * 10 + cur - k)

            numset = res

        return res

