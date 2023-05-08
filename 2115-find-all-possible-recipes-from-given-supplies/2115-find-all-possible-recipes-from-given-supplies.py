class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = {}
        dep = {rec:0 for rec in recipes}
        
        for index,ings in enumerate(ingredients):
            for ing in ings:
                if ing not in graph:
                    graph[ing] = [recipes[index]]


                else:
                    graph[ing].append(recipes[index])

                dep[recipes[index]] += 1

        q = deque(supplies)
        visited = set()
        baked = []
        starter = len(supplies)
        
        while q:
            cur = q.popleft()
            
            if cur in visited:
                continue
                
            if starter==0:
                baked.append(cur)
                
            else:
                starter-=1
            
            if cur in graph:
                for child in graph[cur]:
                    dep[child] -= 1

                    if dep[child]==0:
                        q.append(child)

        return baked
        
        