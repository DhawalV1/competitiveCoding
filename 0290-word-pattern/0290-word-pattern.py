class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s + ' '
        map1 = defaultdict(list)
        map2 = defaultdict(list)
        i = 0
        j = 0
        k = 0
        while i < len(s) and j < len(s):
            if s[j].isalpha():
                j += 1
            else:
                
                map1[s[i:j]].append(k)
                
                k += 1
                j+=1
                i = j
                
        for i in range(len(pattern)):
            map2[pattern[i]].append(i)
    
        a = []
        b = []
        for key in map1.keys():
            a.append(map1[key])
        print(a) 
        for key in map2.keys():
            b.append(map2[key])
            
        return a==b
                
                
        
            
            

        