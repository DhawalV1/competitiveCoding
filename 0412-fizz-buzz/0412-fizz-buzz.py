class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        
        out = ['{}'.format(i) for i in range(1,n+1)]
        
        for i in range(2,n,3):
            out[i] = 'Fizz'
        
                
            
        for i in range(4,n,5):
            out[i] = 'Buzz'
            if (i+1)%3==0:
                out[i] = 'FizzBuzz'
                
            
        
        return out