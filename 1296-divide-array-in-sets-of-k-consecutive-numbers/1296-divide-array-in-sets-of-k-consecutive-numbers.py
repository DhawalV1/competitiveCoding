class Solution:
    def isPossibleDivide(self, hand: List[int], group: int) -> bool:
        n = len(hand)
        groups = n / group
        if int(groups) == groups:
            d = {}
            for i in hand:
                if i in d:
                    d[i] += 1
                else:
                    d[i] = 1
            while groups:
                m = min(d)
                if m in d:
                    v = d[m]
                    for i in range(m, m + group):
                        if i in d:
                            d[i] -= v
                            if d[i] < 0:
                                return False
                            elif d[i] == 0:
                                d.pop(i)                        
                        else:
                            return False
                    else:
                        groups -= v
            else:
                return True
        else:
            return False