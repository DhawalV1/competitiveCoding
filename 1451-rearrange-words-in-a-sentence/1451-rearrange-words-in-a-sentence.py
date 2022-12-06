class Solution:
    def arrangeWords(self, text: str) -> str:
        text += ' '
        mapi = defaultdict(list)
        p = ''
        count = 0
        for i in text:
            
            p += i
            
            if i == ' ':
                mapi[len(p)].append(p)
                p = ''
        a = []   
        for key in mapi.keys():
            a.append(key)
        a.sort()
        p = ''
        
            
        for key in a:
            for i in mapi[key]:
                p += i
                
                
        return p[0:len(p)-1].capitalize()
        print(a)
                
            
        