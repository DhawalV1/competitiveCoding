class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        change = 0
        for i in range(len(digits)):
            if digits[i] != 9:
                change = 1
            
        if change==0:
            return [1] + [0]*len(digits)
        i = len(digits)-1
        
        while i>0:
            
                
            if digits[i] == 9:
                digits[i] = 0
                
            else:
                break
            i -= 1
                
        digits[i] += 1
        
        return digits
            
                
            
        