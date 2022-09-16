class Solution:
    def isPossibleDivide(self, A: List[int], k: int) -> bool:
        c = collections.Counter(A)
        start = collections.deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1: return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == k: opened -= start.popleft()
        return opened == 0