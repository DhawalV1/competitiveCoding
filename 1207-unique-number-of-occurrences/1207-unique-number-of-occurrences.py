from collections import Counter
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        return len([i for i in Counter(arr).values()]) == len(set([i for i in Counter(arr).values()]))