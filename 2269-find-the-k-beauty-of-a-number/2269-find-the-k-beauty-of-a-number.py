class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        
        p = str(num)
        q = int(p[0:k])
        count = 0
        for i in range(len(p)-k+1):
            
            if p[i:k+i].lstrip('0')=='':
                continue
            else:
                q = int(p[i:k+i].lstrip('0'))

                if num%q==0:
                    count += 1
            
        return count
        