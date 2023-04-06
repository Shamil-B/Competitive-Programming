class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        allNodes = set()
        loved = set()
        
        for edge in edges:
            allNodes.add(edge[0])
            allNodes.add(edge[1])
            loved.add(edge[1])
            
        allNodes = list(allNodes)
        
        starters = []
        for node in allNodes:
            if node not in loved:
                starters.append(node)
                
        return starters