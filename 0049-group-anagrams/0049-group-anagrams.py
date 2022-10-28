class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hmap = defaultdict(list)
        for i in strs:
            
            hmap[tuple(sorted(i))].append(i)
        return list(hmap.values())
        
        