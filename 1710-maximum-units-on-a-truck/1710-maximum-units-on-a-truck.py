class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], trucksize: int) -> int:
        boxTypes.sort(key=lambda x:x[1],reverse = True)
        maxi = 0
        i = 0
        while i < len(boxTypes):
            if trucksize - boxTypes[i][0] >= 0:
                maxi = maxi + boxTypes[i][0] * boxTypes[i][1] 
                trucksize -= boxTypes[i][0]
            else:
                maxi = maxi + boxTypes[i][1] * (trucksize)
                return maxi
            i = i+1
        return maxi
    
    
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        units, i = 0, 0
        while truckSize > 0 and i < len(boxTypes):
            units += min(truckSize,boxTypes[i][0]) * boxTypes[i][1]
            truckSize -= boxTypes[i][0]
            i += 1
        return units

        