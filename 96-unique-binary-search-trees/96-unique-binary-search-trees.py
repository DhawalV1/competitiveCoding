class Solution:
    def numTrees(self, n: int) -> int:
        dp ={}

        def ct_tree(l):
            if l<1:return 1

            if l in dp:return dp[l]
            
            
                

            dp[l]=0
            for i in range(1,l+1):
                dp[l] += ct_tree(i-1)*ct_tree(l-i)

            return dp[l]

        return ct_tree(n)
        
        
    