class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        
        x = (hour%12)*30+(minutes/60)*30
        y = minutes/60*360
        print(x,y)
        return min(abs(x-y),360-abs(x-y))
        