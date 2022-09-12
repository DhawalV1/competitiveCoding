class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        mini = float('inf')
        timePoints.sort(key=lambda x:(x[0:2],x[3:]))
        timePoints[0] = int(timePoints[0][0:2])*60 + int(timePoints[0][3:5])
        for i in range(1,len(timePoints)):
            timePoints[i] = int(timePoints[i][0:2])*60 + int(timePoints[i][3:5])
            mini = min(mini,timePoints[i]-timePoints[i-1])
        return min(mini,1440-timePoints[-1]+timePoints[0])
        