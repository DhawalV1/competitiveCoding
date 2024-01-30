class Solution:
    def maximumLength(self, s: str) -> int:
        maxl = -1
        hash = defaultdict(int)
        for i in range(len(s)):
            for j in range(i,len(s)):
                if len(set(s[i:j+1]))==1:
                    hash[s[i:j+1]] += 1
                    
        for key in hash.keys():
            if hash[key]>2:
                maxl = max(len(key),maxl)
        return maxl
                    
                    
        print(hash)
        
            
        