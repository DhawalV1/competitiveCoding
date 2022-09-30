class Solution:
    def flipLights(self, n: int,m: int) -> int:
        
        
        states = {
        'N': 0b000,
        'A': 0b111,
        'O': 0b101,
        'E': 0b010,
        'T': 0b001,
        'AT': 0b111 ^ 0b001,
        'OT': 0b101 ^ 0b001,
        'ET': 0b010 ^ 0b001,
        }
        steps = {
            0: ['N'],
            1: ['A', 'O', 'E', 'T'],
            2: ['N', 'A', 'O', 'E', 'AT', 'OT', 'ET'],
            3: states.keys(),
        }
    
        n, m = min(n, 3), min(m, 3)
        mask = (1 << n) - 1
        ans = set()
        for s in steps[m]:
            ans.add((0b111 ^ states[s]) & mask)
        return len(ans) 
