class Solution:
    
    
   
    
    def getMinString(self,a,b):
        return a if (len(a)<len(b) or (len(a)==len(b) and a<b)) else b
    
    def addTwoStrings(self,a,b):
        if b.find(a) != -1:
            return b
        for i in range(len(a)):
            t1 = a[i:]
            t2 = b[:len(t1)]
            if t1 == t2:
                return a + b[len(t1):]
        return a + b
    
    
    def solve(self,a,b,c): 
        t1 = self.addTwoStrings(a, b)
        t2 = self.addTwoStrings(b, a)
        res1 = self.getMinString(self.addTwoStrings(t1, c),self.addTwoStrings(c, t1))
        res2 = self.getMinString(self.addTwoStrings(t2, c),self.addTwoStrings(c, t2))
        return self.getMinString(res1, res2)
    
    def minimumString(self, a: str, b: str, c: str) -> str:
        
        res = self.getMinString(self.solve(a, b, c),self.solve(b, c, a))
        return self.getMinString(res,self.solve(c,a,b))
    