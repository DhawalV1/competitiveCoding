class Solution:
    def maxProduct(self, s: str) -> int:
        
        
        sz, ans, s1, s2 = len(s), 0, '', ''
        
        @lru_cache(None)
        def solve(i: int, s1: str, s2: str) -> None:
            nonlocal ans, s
            if i >= sz:
                if s1 == s1[::-1] and s2 == s2[::-1]:
                    ans = max(ans, len(s1) * len(s2))
                return
            solve(i + 1, s1, s2)
            s1_pick, s2_pick = s1 + s[i], s2 + s[i]
            solve(i + 1, s1_pick, s2)
            solve(i + 1, s1, s2_pick)
            
        solve(0, s1, s2)
        return ans