class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        #lets construct the graph first
        
        n = len(bombs)
        graph = {"bomb_"+str(i+1):[] for i in range(n)}
        
        for i in range(n):
            x1 = bombs[i][0]
            y1 = bombs[i][1]
            radius = bombs[i][2]
            for j in range(n):
                x2 = bombs[j][0]
                y2 = bombs[j][1]
                if i!=j:
                    distance = math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
                    if distance<=radius:
                        graph["bomb_"+str(i+1)].append("bomb_"+str(j+1))
                        
        # print(graph)
        def detonate(node):
            detonator = [node]
            visited = set()
            bombsDetonated = 0
            while detonator:
                bomb = detonator.pop()
                if bomb in visited:
                    continue
                    
                visited.add(bomb)
                bombsDetonated += 1
                self.explored.add(bomb)
                for otherBomb in graph[bomb]:
                    detonator.append(otherBomb)

            return bombsDetonated
        
        self.explored = set()
        maxBombs = 0
        for bomb in graph.keys():
            if bomb not in self.explored:
                maxBombs = max(maxBombs,detonate(bomb))
                
        return maxBombs