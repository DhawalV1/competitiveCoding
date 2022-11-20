class Solution:
    def calculate(self, s: str) -> int:
        
        temp = 0
        res = 0
        sign = 1
        stack = []
        stack.append(1)
        
        for x in s:
            if x == '+' or x=='-':
                res += sign * temp
                if x == '+': sign = stack[-1]*1
                else: sign = -1*stack[-1]
                temp = 0
            elif x.isdigit():
                temp = temp*10 + int(x)
            elif x=='(':
                stack.append(sign)
            elif x == ')':
                if stack:
                    stack.pop()
            elif x == ' ':
                continue
                
        res += temp * sign
        return res