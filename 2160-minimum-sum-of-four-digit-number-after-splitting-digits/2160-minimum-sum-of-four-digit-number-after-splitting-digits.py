class Solution:
    def minimumSum(self, num: int) -> int:
        num = str(num)
        a = int(num[0])
        b = int(num[1])
        c = int(num[2])
        d = int(num[3])
        
        arr = [a,b,c,d]
        arr.sort()
        x = arr[0]
        y = arr[1]
        z = arr[2]
        w = arr[3]
        
        return x*10+z + y*10 + w
        