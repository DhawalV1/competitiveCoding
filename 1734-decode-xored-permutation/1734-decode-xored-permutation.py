class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n= len(encoded)+1
        p = reduce(operator.xor,range(1,n+1))
        q = 1
        x = 0
        while q < n:
            x ^= encoded[q]
            q  += 2
        perm = []
        perm.append(p^x)
        i = 0
        while i!=len(encoded):
            perm.append(encoded[i]^perm[-1])
            i += 1
        return perm
        
        
        