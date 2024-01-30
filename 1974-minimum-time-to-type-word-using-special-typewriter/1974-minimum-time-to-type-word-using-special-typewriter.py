class Solution:
    def minTimeToType(self, word: str) -> int:
        
        if word[0]=='a': 
            count = 1 
        else:
            count = 0
        init ='a'
        if count == 0:
            for i in word:
                if abs(ord(i)-ord(init)) > 13:
                    
                    count += (26 - abs(ord(i)-ord(init)))+1
                    
                else:
                    count += abs(ord(i)-ord(init))+1
                init = i
                
                
                
        else:
            for i in word[1::]:
                if abs(ord(i)-ord(init)) > 13:
                    
                    count += (26 - abs(ord(i)-ord(init)))+1
                    
                else:
                    count += abs(ord(i)-ord(init))+1
                init = i
        return count
            
        