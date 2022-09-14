from collections import Counter
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort(reverse=True)
    
        return sum(i<j for i,j in enumerate(citations))
        
        
        
        