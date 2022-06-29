class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        
        
        stack = []
        for digit in num:
            while k and stack and stack[-1]>digit:
                stack.pop()
                k -= 1
            stack.append(digit)
            
        while k>0:
            stack.pop()
            k -= 1
            
        while stack and stack[0] == '0':
            stack.pop(0)
            
        if stack:
            return "".join(stack)
        else:
            return '0'
                
        
        
        
        