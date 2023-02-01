class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        if str1+str2!=str2+str1:
            return ''
        
        elif str1==str2:
            return str1
        
        else:
            
            lgcd = math.gcd(len(str1),len(str2))
            
            return str1[:lgcd]
            
            