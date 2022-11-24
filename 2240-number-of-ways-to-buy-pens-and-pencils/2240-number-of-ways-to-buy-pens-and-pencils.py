class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        count = 0
        n = 0
        while(total-cost1*n>0):
            count += (total - cost1*n)//cost2 + 1
            n += 1
          
        if total%cost1==0: return count + 1
        return count