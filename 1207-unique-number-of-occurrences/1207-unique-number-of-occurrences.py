# from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #print(Counter(arr))
        return (lambda x: len(x) == len(set(x)))(collections.Counter(arr).values())