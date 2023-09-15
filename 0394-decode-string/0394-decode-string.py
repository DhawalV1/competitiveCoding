class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = ['']
        it,num = 0,0
        for i in s:
            if i == '[':
                stack.append(num)
                num = 0
                stack.append('')
                
            elif i == ']':
                str1 = stack.pop()
                rep = stack.pop()
                str2 = stack.pop()
                stack.append(str2 + str1*rep)
                
            elif i.isdigit():
                num = num*10+int(i)
            else:
                stack[-1] += i
                
        return ''.join(stack)
                

                
            
        