class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        loved = set()
        
        for edge in edges:
            loved.add(edge[1])
 
        starters = set()
        for edge in edges:
            if edge[0] not in loved:
                starters.add(edge[0])
            if edge[1] not in loved:
                starters.add(edge[1])
                
        return list(starters)