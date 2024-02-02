class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        p = []
        for i in range(len(str(low)),len(str(high))+1):
            p = p+self.gen(i)
        
        return [i for i in p if i>=low and i<=high]
    def gen(self,n):
        a = []
        for i in range(1,10-n+1):
            s = ''
            for j in range(i,i+n):
                s = s+str(j)
                
            a.append(int(s))
            
        return a
            
            
            