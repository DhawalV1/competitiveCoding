class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key=lambda x: (x[0],-x[1]))
        print(properties)
        mini = 0
        ans = 0
        for i in range(len(properties)-1,-1,-1):
            if properties[i][1] < mini:
                ans += 1
            mini = max(mini,properties[i][1])
               
        return ans
        
        
        
        
        
        
            
        
        