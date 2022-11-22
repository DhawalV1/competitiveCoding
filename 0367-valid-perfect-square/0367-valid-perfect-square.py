class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        
        for i in range(1,47000):
            if i*i>=num:
                if i*i==num:
                    return True
                else:
                    return False
        