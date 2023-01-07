class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        start = 0
        cb = 0
        rb = 0
        
        for i in range(len(cost)):
            
            cb += gas[i] - cost[i]
            
            if cb < 0:
                start = i + 1
                rb += cb
                cb = 0
                
        return start if (cb + rb)>=0 else -1
        
       
        