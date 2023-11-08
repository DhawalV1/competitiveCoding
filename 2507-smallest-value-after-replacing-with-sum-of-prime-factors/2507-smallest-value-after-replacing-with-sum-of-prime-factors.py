class Solution:
    def smallestValue(self, n: int) -> int:
        if n == 4: return 4
        def isprime(p):
            for i in range(2,int(p**0.5)+1):
                if p%i==0:
                    return False
            return True
        def give_sof(num):
            i = 2
            sumi = 0
            while num!=1:
                if num%i==0:
                    sumi += i
                    num = num//i
                    i = 1
                i += 1
            return sumi
        ans = 0
        if isprime(give_sof(n))==True:
            return give_sof(n)
        else:
            return self.smallestValue(give_sof(n))
            
        
        
            
            
        