class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [d for c,d in sorted([[a, b] for a, b in zip(heights,names)])][::-1]
