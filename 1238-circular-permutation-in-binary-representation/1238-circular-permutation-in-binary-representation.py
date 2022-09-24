class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        return [start^i^i>>1 for i in range(1<<n)]
    
    # i^i>>1 is code for generating binary from 0 to 2**n-1
    