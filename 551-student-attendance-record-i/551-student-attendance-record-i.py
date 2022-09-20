class Solution:
    def checkRecord(self, s: str) -> bool:
        absent=s.count("A")
        if absent>=2 or "LLL" in s:
            return False
        return True
            