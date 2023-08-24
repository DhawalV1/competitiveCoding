class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        
        deck.sort(reverse=True)
        
        q = deque()
        
        for c in deck:
            
            if q:
                
                q.appendleft(q.pop())
                
            q.appendleft(c)
            
        return q
        
        