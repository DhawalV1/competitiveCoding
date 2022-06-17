class Solution:
    def recurParenthesis(self, ret: str, l, r, ans: List[str]):

	# l and r denote the number of left and right parenthesis remaining.
        if l == 0 and r == 0:
            ans.append(ret)
        # if having enough left parenthesis
        if l > 0:
            self.recurParenthesis(ret+"(", l-1, r, ans)
        # if right parenthesis remaining > left parenthesis remaining(so that it could be matched)
        if r > l:
            self.recurParenthesis(ret+")", l, r-1, ans)
        return ans
    
    def generateParenthesis(self, n: int) -> List[str]:
        return self.recurParenthesis("(", n-1, n, [])
        
        
   