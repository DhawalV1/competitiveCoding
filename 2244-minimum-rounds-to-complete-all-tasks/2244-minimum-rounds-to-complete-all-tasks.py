class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        maxi = 0
        count = {}
        for i in tasks:
            if i in count:
                count[i] += 1
            else:
                count[i] = 1
                
        for key in count.keys():
            
            if count[key]<2:
                return -1
            else:
                maxi += (count[key]-1)//3+1
                
                
        return maxi