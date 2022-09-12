class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        arr = set()
        for time in timePoints:
            hr,minu = time.split(":")
            number = int(hr)*60 + int(minu)
            if number in arr:
                return 0
            arr.add(number)
            
        arr = sorted(arr)
        out = 1440
        for i in range(1,len(arr)):
            out = min(out,arr[i]-arr[i-1])
            
        return min(out,1440-arr[-1]+arr[0])
            
        
        
   