class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        
        result = []
        
        for i in queries:
            result.append(self.generatePalindrome(intLength, i))
        
        return result
    
    def generatePalindrome(self, length, num):
        
        index = num -1
        
	
        if length % 2 == 0:
            cur = int('1' + '0' * (length // 2 -1))
            maxLength = len(str(cur))
            cur += index
            
            if len(str(cur)) > maxLength:
                return -1
            
            else:
                cur = str(cur)
                cur = cur + cur[::-1]
                cur = int(cur)
                return cur
				
        
        else:
            cur = int('1' + '0' * (length // 2))
            maxLength = len(str(cur))
            cur += index
            
            if len(str(cur)) > maxLength:
                return -1
            
            else:
                cur = str(cur)
                temp = str(cur)[:-1]
                cur = cur + temp[::-1]
                cur = int(cur)
                return cur