class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0:return 0
        if num<0:
            num = sorted(str(-num),reverse=True)
            p = ''
            for i in num:
                p += i
            

    
        

            return -1*int(p)
        else: num = sorted(str(num))
        p = ''
        for i in num:
            p += i
        print(num,p)
        
        l = p.count('0')
        print(l)
        k = p[l] + '0'*l + p[l+1::]
        
        return k
        