class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        
        def dfs(eid):
            if manager[eid]!=-1:
                informTime[eid]+=dfs(manager[eid])
                manager[eid]=-1
            return informTime[eid]
        for eid in range(n):
            dfs(eid)
        return max(informTime)
    
        ''''
        if n <= 1:
            return 0
        rst = 0
        childs = defaultdict(list)
        for idx, parent in enumerate(manager):
            childs[parent].append(idx)

        q = deque([(headID, informTime[headID])])
        while q:
            cur_id, cur_time = q.popleft()
            # calculate max
            rst = max(rst, cur_time)
            for child in childs[cur_id]:
                q.append((child, cur_time + informTime[child]))
        return rst 
        '''