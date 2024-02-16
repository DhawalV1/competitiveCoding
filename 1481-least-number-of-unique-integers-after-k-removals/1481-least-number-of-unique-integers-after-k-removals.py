class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
        val = sorted([i for i in collections.Counter(arr).values()])
        print(val)
        count = 0
        i = 0
        while k>0:
            k = k - val[i]
            if k>-1:
                count += 1
            i += 1
        return len(val)-count