class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        finArr = [0]*n
        graph = defaultdict(list)

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node,parent):
            if node not in graph:
                return {labels[node] : 1}
            
            dic = defaultdict(int)
            for child in graph[node]:
                if child!= parent:
                    d = dfs(child,node)
                    for k in d:
                        dic[k] += d[k]
            

            finArr[node] = dic[labels[node]] + 1
            dic[labels[node]] += 1
            return dic



        dfs(0,-1)
        for i in range(len(finArr)):
            if finArr[i] == 0:
                finArr[i] = 1
        

        return finArr
            