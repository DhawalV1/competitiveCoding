class Solution:
    def largestPalindrome(self, n: int) -> int:
        
        
        
        if n==1: return 9
        if n==2: return 987
        if n>3 and n%2==0:
            m = 0
            for i in range(n):
                m = m*10+9
            print(m)
            l = 0
            for i in range(n//2):
                l = l*10+9
            for k in range(n//2):
                l = l*10
            return ((m%1337)*(l+1)%1337)%1337
        else:
            for z in range(2, 2 * (9 * 10**n) - 1):
                left = 10**n - z
                right = int(str(left)[::-1])
                root_1, root_2 = 0, 0

                if z**2 - 4*right < 0:
                    continue
                else:
                    root_1 = 1/2 * (z + (z**2-4*right)**0.5)
                    root_2 = 1/2 * (z - (z**2-4*right)**0.5)
                    if root_1.is_integer() or root_2.is_integer():
                        return (10**n*left+right) %1337