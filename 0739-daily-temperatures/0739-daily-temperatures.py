class Solution:
    def dailyTemperatures(self,temperatures: List[int]) -> List[int]:
        
        stack = []
        wait = [0]*len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                wait[j] = i-j
            stack.append(i)
        return wait
        '''
        t.append(0)
        res = []
        i = 0
        j = i + 1
        while i<j and j<len(t):
            while t[i]>=t[j] and j!=len(t)-1:
                j = j+1
            else:
                if t[i]<t[j]: 
                    res.append(j-i)
                    i = i+1
                    j = i+1
                else:
                    res.append(0)
                    i = i+1
                    j = i+1
                    
            
        
        return res
        
        '''