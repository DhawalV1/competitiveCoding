class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        
        rc1 = 0
        for i in s:
            if i == '1':
                rc1 += 1
        rc0 = len(s) - rc1
        print(rc0,rc1)
        lc0 = lc1 = 0
        mini = lc1+rc0
        for i in range(len(s)):
            if s[i]=='0':
                lc0 += 1
                rc0 -= 1
            else:
                lc1 += 1
                rc1 -= 1
            mini = min(mini,rc0+lc1)
        return mini