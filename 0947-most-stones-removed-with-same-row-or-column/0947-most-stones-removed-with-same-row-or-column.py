class UnionFind:
    def __init__(self,arr):
        self.representatives = {tuple(item):tuple(item) for item in arr}
        self.heights = {tuple(item):1 for item in arr}

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
        xRep = self.find(x)
        yRep = self.find(y)

        height1 = self.heights[xRep]
        height2 = self.heights[yRep]

        if height1 > height2:
            newRep = xRep
            oldRep = yRep

        else:
            newRep = yRep
            oldRep = xRep
            
        if oldRep==newRep:
            return

        self.representatives[oldRep] = newRep
        self.heights[newRep] = height1+height2


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        uf = UnionFind(stones)
        for stone1 in stones:
            stone1 = tuple(stone1)
            for stone2 in stones:
                stone2 = tuple(stone2)
                if stone1!=stone2 and (stone1[0]==stone2[0] or stone1[1]==stone2[1]):
                    uf.union(stone1,stone2)
            
        usedSoFar = set()
        size = 0
        for stone in stones:
            rep = uf.find(tuple(stone))
            if rep not in usedSoFar:
                usedSoFar.add(rep)
                size += (uf.heights[rep]-1)
                
        return size