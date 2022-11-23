class Solution:
    def getAverages(self, num: List[int], k: int) -> List[int]:
        
        p = [0]
        for i in range(len(num)):
            p.append(p[-1]+num[i])
        n = len(num)   
        for i in range(len(num)):
            if i<k or i>n-k-1: num[i] = -1
            else: num[i] = (p[i+k+1]-p[i-k])//(2*k+1)
        return num