class Solution:
    def canChange(self, start: str, end: str) -> bool:
        if [i for i in start if i is not '_']!=[i for i in end if i is not '_']:
            return False
        ls = []
        rs = []
        le = []
        re = []
        for i in range(len(start)):
            if start[i]=='L':
                ls.append(i)
            if start[i]=='R':
                rs.append(i)
        for i in range(len(end)):
            if end[i]=='L':
                le.append(i)
            if end[i]=='R':
                re.append(i)
        if len(ls)!=len(le) or len(rs)!=len(re):
            return False
        for i in range(len(ls)):
            if ls[i]<le[i]:
                return False
        for i in range(len(rs)):
            if rs[i]>re[i]:
                return False
        return True
        
        
        
        
        
        if [i for i in start if i is not '_']!=[i for i in end if i is not '_']:
            return False
        
        