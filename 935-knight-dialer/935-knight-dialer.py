class Solution:
    def knightDialer(self, n: int) -> int:
        k = 10**9 + 7
        hop = [1]*10
        if n==1:
            return sum(hop)
        
        old = [1]*10
        for i in range(n-1):
            for j in range(10):
                old[j] = hop[j]
            hop[1] = (old[6]+old[8]) % k
            hop[2] = old[7]+old[9] % k
            hop[3] = (old[4]+old[8]) % k
            hop[4] = (old[3]+old[9]+old[0]) % k
            hop[5] = 0
            hop[6] = (old[1]+old[7]+old[0]) % k
            hop[7] = (old[2]+old[6]) % k
            hop[8] = (old[1]+old[3]) % k
            hop[9] = (old[4]+old[2]) % k
            hop[0] = (old[4]+old[6]) % k
            
        return sum(hop)%k
            
        
        
        
        
    
    