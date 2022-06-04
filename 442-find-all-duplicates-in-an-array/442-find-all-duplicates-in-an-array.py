class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        t = []
        for key,value in freq.items():
            if value == 2:
                t.append(key)
        return t
        