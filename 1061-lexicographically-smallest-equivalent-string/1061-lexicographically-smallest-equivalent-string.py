class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        n = len(s1)
        self.representatives = {ch:ch for ch in s1+s2+baseStr}
            
        # now for every pair of characters we are going to construct the union graph

        for i in range(n):
            self.union(s1[i],s2[i])

        smallestStr = ""
        for ch in baseStr:
            smallestStr += self.find(ch)
            
        return smallestStr
    
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
        newRep = self.find(x)
        oldRep = self.find(y)

        if newRep > oldRep:
            newRep,oldRep = oldRep,newRep

        self.representatives[oldRep] = newRep