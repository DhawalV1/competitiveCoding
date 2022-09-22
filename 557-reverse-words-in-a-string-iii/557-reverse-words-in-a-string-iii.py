class Solution:
    def reverseWords(self, s: str) -> str:
        p = ''
        sq = s.split(' ')
        
        for i in range(len(sq)-1):
            p = p + sq[i][::-1] + ' '
        p = p + sq[-1][::-1]
            
        return p