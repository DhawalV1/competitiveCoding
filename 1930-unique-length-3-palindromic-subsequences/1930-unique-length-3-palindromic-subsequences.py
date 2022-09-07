class Solution:
    def countPalindromicSubsequence(self, stri: str) -> int:
        p = []
        maxi = 0
        for i in range(len(stri)):
            if stri[i] not in p:
                p.append(stri[i])
                count = 0
                j = len(stri)-1
                while j < len(stri) and j > i+1:
                    if stri[j] == stri[i]:
                        maxi = maxi + len(set(stri[i+1:j]))
                        break
                    j = j - 1
        return maxi
                    
                    
                
        