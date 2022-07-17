class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        p = int(current[0:2])*60 + int(current[3:5])
        q = int(correct[0:2])*60 + int(correct[3:5])
        
        r = q-p
        if r<0:
            r = 24*60-r
        k = 0
        if r>=60:
            k = r//60
            r = r%60
        
        if r>=15:
            k = k + r//15
            r = r%15
        if r>=5:
            k = k+r//5
            r = r%5
        if r>=1:
            k = k + r
        return k
        
        