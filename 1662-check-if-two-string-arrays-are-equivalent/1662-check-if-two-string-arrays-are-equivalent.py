class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        p = 'a'
        q = 'a'
        for c in word1:
            
            p += c
        for d in word2:
            q +=  d;
        if len(p)!=len(q): return False
        i = 0
        while(i<len(p)):
            if p[i]!=q[i]:
                return False
            i = i+1
        return True