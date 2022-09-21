class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        mini = min([len(i) for i in strs]) 
        d = True
        a = ''
        for i in range(mini):
            for j in range(len(strs)-1):
                if strs[j][i]!=strs[j+1][i]:
                    d = False
                    break
            if d:
                a = a + strs[j][i]
                
        return a
        