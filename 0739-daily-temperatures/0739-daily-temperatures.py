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
        
        