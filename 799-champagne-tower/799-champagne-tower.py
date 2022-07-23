class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        currow = [poured]
        for i in range(query_row+1):
            nextRow = [0]*(i+2)
            for j in range(i+1):
                if currow[j]>=1:
                    nextRow[j] += (currow[j]-1)/2.0
                    nextRow[j+1] += (currow[j]-1)/2.0
                    currow[j] = 1
            if i!=query_row:
                currow = nextRow
        return currow[query_glass]