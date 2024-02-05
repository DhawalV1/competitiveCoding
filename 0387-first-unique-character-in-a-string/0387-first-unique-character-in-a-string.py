class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
                
        for key in d.keys():
            if d[key]==1:
                return s.index(key)
        return -1
            
        