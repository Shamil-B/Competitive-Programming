class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        freq = {}
        n = len(edges)

        for edge in edges:
            if edge[0] not in freq:
                freq[edge[0]] = 1
                
            else:
                freq[edge[0]] += 1
                
            if edge[1] not in freq:
                freq[edge[1]] = 1
                
            else:
                freq[edge[1]] += 1
                
                
        for item in freq.items():
            if item[1] == n:
                return item[0]