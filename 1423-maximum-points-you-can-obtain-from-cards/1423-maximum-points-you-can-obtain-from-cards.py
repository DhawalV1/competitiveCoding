class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        new_list=[]
        n  = len(cardPoints)
        j=0
        for i in range(0,len(cardPoints)):
            j = j + cardPoints[i]
            new_list.append(j)
        
        mini= new_list[n-k-1]
        for i in range(1,k+1):
            mini = min(new_list[i+n-k-1]-new_list[i-1],mini)
        return new_list[-1] - mini
            