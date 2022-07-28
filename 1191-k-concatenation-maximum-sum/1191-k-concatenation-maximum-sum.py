class Solution:
    mod = 10**9 + 7
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
        mod = 10**9 + 7
        if k == 1:
            return self.kanade(arr) % mod
        if k == 2:
            return self.kanade(arr+arr) % mod
        sumi = sum(arr)
        if sumi <= 0:
            return self.kanade(arr+arr+arr) % mod
        else:
            return (self.kanade(arr+arr) + (k-2)*sumi) % mod 
        
    def kanade(self,arr):
        mod = 10**9 + 7
        maxi = float('-inf')
        maxie = 0
        for i in range(len(arr)):
            maxie = maxie + arr[i]
            if maxi < maxie:
                maxi = maxie
            if maxie < 0:
                maxie = 0
        if maxi < 0:
            return 0
        else:
            return maxi % mod
        
        
        
        
        
       
        