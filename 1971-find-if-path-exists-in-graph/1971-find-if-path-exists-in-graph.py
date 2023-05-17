class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # we do the union find
        
        self.representatives = {i:i for i in range(n)}
        self.heights = {i:1 for i in range(n)}
            
        # now for every edge we are going to construct the union graph
        
        for node1,node2 in edges:
            self.union(node1,node2)

                
        # finally we check and return if the source and destination have the same representative meaning same group meaning they are connected meaning there is a path between them :D

        return self.find(source)==self.find(destination)
    
    def find(self,x):
        rep = x
        
        while self.representatives[rep]!=rep:
            rep = self.representatives[rep]

        topRep = rep
        rep = x

        while self.representatives[rep]!=rep:
            curNode = rep
            rep = self.representatives[rep]
            self.representatives[curNode] = topRep

        return topRep
        
    def union(self,x,y):
        height1 = self.heights[x]
        height2 = self.heights[y]

        newHeight = max(height1,height2)

        if height1 == height2:
            newHeight = height1+1

        if height1 > height2:
            newRep = self.find(x)
            oldRep = self.find(y)

        else:
            newRep = self.find(y)
            oldRep = self.find(x)

        self.representatives[oldRep] = newRep
