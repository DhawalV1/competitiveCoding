class Solution:
    def maximumEvenSplit(self, f: int) -> List[int]:
        if f%2==1:
            return []
        if f==2:
            return [2]
        sumi = 0
        i = 2
        a = []
        sumi1 = 0
        while sumi <= f:
            if sumi + i <= f:
                a.append(i)
                sumi1 += i
            sumi = sumi + i
            i = i + 2
        a[-1] = a[-1] + (f-sumi1)
        return a
        