class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # we do the union find
        
        self.representatives = {i:i for i in range(1,n+1)}
        self.heights = {i:1 for i in range(1,n+1)}
        
        # the only additional lines to the normal union find template are 3
        # ----------------here--------------#

        self.costs = {i:float(inf) for i in range(1,n+1)}

        # now for every edge we are going to construct the union graph
        for city1,city2,cost in roads:
            self.union(city1,city2,cost)

        # ----------------here--------------#
        return self.costs[self.find(1)]

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
        
    def union(self,x,y,cost):
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
        
        # ----------------and here--------------#
        self.costs[newRep] = min(self.costs[newRep],self.costs[oldRep],cost)
