class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        
        l = event1[0][0:2]*60 + event1[0][3:5]
        r = event1[1][0:2]*60 + event1[1][3:5]
        
        a = event2[0][0:2]*60 + event2[0][3:5]
        b = event2[1][0:2]*60 + event2[1][3:5]
        
        if (l<=a and a<=r) or (l<=b and b<=r) or (a<=l and b>=r):
            return True
        else:
            return False