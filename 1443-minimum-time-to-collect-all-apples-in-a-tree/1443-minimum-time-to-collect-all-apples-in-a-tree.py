class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        graph = defaultdict(list)
        
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        ans = 0
        visited = set()
        def dfs(node):
            nonlocal ans
            
            if (not any(hasApple)):                
                return
            
            if node in visited:
                return False
                
            visited.add(node)
            ans += 1

            found = hasApple[node]
            hasApple[node] = False
            for neig in graph[node]:
                if dfs(neig):
                    found = True
                
            if not found:
                visited.remove(node)
                ans -= 1
                return False
            
            return True
           
        dfs(0)
        return max((ans-1)*2,0)
