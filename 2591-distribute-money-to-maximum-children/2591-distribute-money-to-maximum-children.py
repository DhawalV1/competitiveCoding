class Solution:
    def distMoney(self, m: int, c: int) -> int:
        ans = 0
        if m<c:return -1
        if m>8*c: return c-1
        
        while (m>0 and m-8>=c-1):
            ans += 1
            m -= 8
            c -= 1
            
        if (m==4 and c==1):
            ans -= 1
            
            
        
        return ans
        