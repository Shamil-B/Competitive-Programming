class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        # contruct the graph first
        graph = [[] for i in range(n)]
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # how many of my subtrees are divisible by k
        def solve(node, parent):
            total_sum = values[node]
            total_ans = 0

            for neig in graph[node]:
                if neig != parent:
                    current_sum, current_ans = solve(neig, node)
                    total_sum += current_sum
                    total_ans += current_ans
                    
            if total_sum % k == 0:
                total_ans += 1

            return total_sum, total_ans

        return solve(0, -1)[1]