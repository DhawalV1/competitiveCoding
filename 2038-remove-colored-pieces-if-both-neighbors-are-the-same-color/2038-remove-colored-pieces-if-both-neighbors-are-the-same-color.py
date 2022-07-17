class Solution:
    def winnerOfGame(self, c: str) -> bool:
        counta = countb = 0
        for i in range(len(c)-2):
            if c[i]=='A' and c[i+1]=='A' and c[i+2]=='A':
                counta = counta + 1
            elif c[i]=='B' and c[i+1]=='B' and c[i+2]=='B':
                countb += 1
        if counta <=countb:
            return False
        if counta > countb:
            return True
        