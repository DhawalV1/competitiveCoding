class Solution:
    def minimumDeletions(self, s: str) -> int:
        if len(s) < 2:
            return 0
        
        count = 0
        for i in s:
            if i == 'a':
                count = count + 1
        if len(s) == count:
            return 0
        
        
        la = 0
        lb = 0
        ra = count
        rb = len(s)-count
        mini = lb + ra
        if len(s) == rb:
            return 0
        for i in range(len(s)):
            
            if s[i] == 'a':
                la = la+1
                ra = ra - 1
            else:
                lb = lb + 1
                rb = rb - 1
            mini = min(lb+ra,mini)
            
        return mini