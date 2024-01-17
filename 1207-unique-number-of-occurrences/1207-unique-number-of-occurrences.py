# from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        #print(Counter(arr))
        return len(collections.Counter(arr).values()) == len(set(collections.Counter(arr).values()))