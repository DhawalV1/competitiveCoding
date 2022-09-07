class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        lenh = (len(arr)+1)//2
        x = {}
        for i in arr:
            if i in x:
                x[i] += 1
            else:
                x[i] = 1
        
        sorted_x = sorted(x.items(), key=operator.itemgetter(1),reverse=True)
        print(sorted_x)
        sumi = 0
        count = 0
        for a,b in sorted_x:
            sumi += b
            count += 1
            if sumi>=lenh:
                return count
                
            
                
       