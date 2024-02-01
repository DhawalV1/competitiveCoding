from collections import defaultdict
class Solution:
    def maximumLength(self, s: str) -> int:
        '''
        s += '0'
        seen = defaultdict(list)
        count = 1
        for i in range(len(s)-1):
            
            if s[i]==s[i+1]:
                
                count += 1
                
            else:
                seen[s[i]].append(count)
                
                
                count = 1
        print(seen)
        maxl = 0
        
    def check(self,arr):
        if len(arr)==1:
            return arr[0]-2
        '''
        special_substrings = defaultdict(int)
        
        start = 0
        while start < len(s):
            curr = start
            while curr < len(s) - 1 and s[curr] == s[curr + 1]:
                curr += 1
            
            window_size = curr + 1 - start
            for length in range(1, window_size + 1):
                special_substrings[(s[start], length)] += window_size + 1 - length
                
            start = curr + 1
        
        
        res = -1
        for k in special_substrings:
            if special_substrings[k] >= 3:
                res = max(res, k[1])
                
        return res
        
                
                

                
            
        