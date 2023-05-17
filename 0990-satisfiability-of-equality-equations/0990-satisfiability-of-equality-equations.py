class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        
        n = 26
        # we do the union find
        self.representatives = {chr(97+i):chr(97+i) for i in range(n)}
        self.heights = {chr(97+i):1 for i in range(n)}
        
        equations.sort(key=lambda equation:equation[1],reverse=True)
            
        # now for every edge we are going to construct the union graph
        for equation in equations:
            variable1 = equation[0]
            variable2 = equation[-1]
            equality = equation[1:3] == '=='

            if not self.union(variable1,variable2,equality):
                return False

        return True
    
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
        
    def union(self,x,y,isEqual):
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
            
        if not isEqual and newRep==oldRep:
            return False

        if isEqual:
            self.representatives[oldRep] = newRep
        return True
