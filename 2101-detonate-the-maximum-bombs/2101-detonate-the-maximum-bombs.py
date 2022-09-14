class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n  =len(bombs)
        max_ans = 0
        G = defaultdict(list)
        for i in range(n):
            for j in range(n):
                if i == j:continue
                if (bombs[i][0] - bombs[j][0])**2 + (bombs[i][1] - bombs[j][1])**2 <= bombs[i][2]**2:
                    G[i].append(j)
                
        for start in range(n):
            this_ans = 0
            q = [start]
            vis = set([start])
            while q:
                pos = q.pop()
                this_ans += 1
                for neib in G[pos]:
                    if neib not in vis:
                        q.append(neib)
                        vis.add(neib)
                        
            max_ans = max(max_ans,this_ans)
            
            if max_ans == n:
                return n
        return max_ans
        