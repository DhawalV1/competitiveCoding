class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        
        index = score.copy()
        index.sort(reverse=True)
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"] + [str(i + 1) for i in range(3, len(score))]
        dic = {}
        for i in range(len(index)):
            dic[index[i]] = medal[i]
        return [dic[i] for i in score]