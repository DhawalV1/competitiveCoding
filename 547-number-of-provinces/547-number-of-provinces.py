class Solution:
    def findCircleNum(self, isc: List[List[int]]) -> int:
        if not isc:
            return 0
        n = len(isc)
        leads = []
        for i in range(n):
            leads.append(i)
        
        groups = n
        for i in range(n):
            for j in range(i+1,n):
                if isc[i][j]:
                    lead1 = self.find(i,leads)
                    lead2 = self.find(j,leads)
                    if lead1 != lead2:
                        leads[lead1] = lead2
                        groups -= 1
        return groups
    
    def find(self,x,parents):
        if x == parents[x]:
            return x
        else:
            return self.find(parents[x],parents)
        
        
        
        
        
      