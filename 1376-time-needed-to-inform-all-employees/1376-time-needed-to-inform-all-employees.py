class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n == 1: return 0

        adj = {i: [] for i in range(n)}

        for i in range(n):
            if i != headID:
                adj[manager[i]].append(i)
        
        que = deque()
        que.append((headID, 0))
        vis = [0] * n
        vis[headID] = 1
        ans = 0
        while que:
            node, time = que.popleft()
            ans = max(ans, time)
            for nod in adj[node]:
                if vis[nod] == 0:
                    que.append((nod, time + informTime[node]))
                    vis[nod] = 1
        
        return ans