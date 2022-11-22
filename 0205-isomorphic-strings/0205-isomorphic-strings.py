class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        mapi = defaultdict(list)
        mapi2 = defaultdict(list)
        
        for i in range(len(s)):
            mapi[s[i]].append(i)
            mapi2[t[i]].append(i)
        a = []
        b = []
        for key in mapi.keys():
            a.append(mapi[key])
        for key in mapi2.keys():
            b.append(mapi2[key])
            
            
        return a == b
        
            
            
            
        