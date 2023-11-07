class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        
        time = []
        
        for i in range(len(dist)):
            
            time.append((dist[i]-1)//speed[i])
            
        time.sort()
        print(time)
        
        for i in range(len(time)):
            
            if time[i]<i:
                
                return i
            
        return len(dist)
            
        
        
                
                
                
            
            
            
        