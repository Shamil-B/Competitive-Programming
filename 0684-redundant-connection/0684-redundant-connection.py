class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        self.representatives = {i:i for i in range(1,n+1)}
        self.heights = {i:1 for i in range(1,n+1)}
            
        # now for every edge we are going to construct the union graph
        self.ans = None
        for node1,node2 in edges:
            self.union(node1,node2)

        return self.ans
    
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
            
        if newRep == oldRep:
            self.ans = [x,y]

        self.representatives[oldRep] = newRep
