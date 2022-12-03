class Solution:
    def frequencySort(self, s: str) -> str:
        
        x = collections.Counter(s)
        
        x = sorted(x.items(),key = lambda y:y[1],reverse = True)
        print(x)
        p = ''
        for key,i in x:
            p += key*i
            
        return p