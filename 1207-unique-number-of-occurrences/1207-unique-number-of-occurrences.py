# from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #print(Counter(arr))
        return len([i for i in collections.Counter(arr).values()]) == len(set([i for i in collections.Counter(arr).values()]))