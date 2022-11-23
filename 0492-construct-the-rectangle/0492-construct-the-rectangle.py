class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        if area == 1:return [1,1]
        factor = []
        for i in range(1,int(sqrt(area))+1):
            if area%i==0:
                factor.append(i)
        print(factor)
        mini = []
        for k in factor:
            mini.append(abs(area//k-k))
        print(mini)
            
        mini1 = float('inf')
        for i in range(len(factor)):
            if mini[i]<mini1:
                mini1 = mini[i]
                k = i
        print(k)
        
        return [area//factor[k],factor[k]]