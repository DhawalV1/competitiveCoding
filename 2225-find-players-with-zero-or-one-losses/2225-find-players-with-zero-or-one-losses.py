class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        
        
        win = set()
        lose = set()
        mapi = defaultdict(lambda:0)
        for i in matches:
            win.add(i[0])
            lose.add(i[1])
            mapi[i[1]] += 1
            
        b = sorted([key for key in mapi.keys() if mapi[key]==1])
        c = sorted(list(win.difference(lose)))
        return [c,b]
        