class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = {}
        for person in dislikes:
            if person[0] not in graph:
                graph[person[0]] = [person[1]]

            else:
                graph[person[0]].append(person[1])


            if person[1] not in graph:
                graph[person[1]] = [person[0]]

            else:
                graph[person[1]].append(person[0])

        dislikeDic = {}
        def biPartite(node,visited=None):
            if not visited:
                visited = set()

            if node in visited:
                return True

            visited.add(node)
            self.explored.add(node)
            for neigh in graph[node]:
                    if neigh in dislikeDic:
                        if node not in dislikeDic:
                            dislikeDic[node] = True
                        if dislikeDic[neigh]==dislikeDic[node]:
                            return False
                    else:
                        if node not in dislikeDic:
                            dislikeDic[node] = True
                        dislikeDic[neigh] = not dislikeDic[node]

                    if not biPartite(neigh,visited):
                        return False

            
            return True

        self.explored = set()
        for key in graph.keys():
            if key not in self.explored:
                if not biPartite(key):
                    return False

        return True

        return True