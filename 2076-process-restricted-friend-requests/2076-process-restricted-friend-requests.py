class Solution:
    def friendRequests(self, n: int, restrictions: List[List[int]], requests: List[List[int]]) -> List[bool]:
        
        self.restrictions = restrictions
        self.representatives = [i for i in range(n)]
        self.size = [1 for i in range(n)]
        
        answerArray = []
        for req in requests:
            successStatus = self.union(req[0],req[1])
            answerArray.append(successStatus)

        return answerArray

    def find(self,x):
        rep = x
        while self.representatives[rep]!=rep:
            rep = self.representatives[rep]

        topRep = rep
#         rep = x

#         while self.representatives[rep]!=rep:
#             curNode = rep
#             rep = self.representatives[rep]
#             self.representatives[curNode] = topRep

        return topRep
        
    def union(self,x,y):
        # if (x,y)==(0,5):
        #     print(self.representatives)
        newRep = self.find(x)
        oldRep = self.find(y)

        size1 = self.size[newRep]
        size2 = self.size[oldRep]
        
        # print('...',self.representatives,oldRep,newRep)
        if newRep==oldRep:
            return True
    
        if size1 < size2:
            newRep,oldRep = oldRep,newRep

        self.representatives[oldRep] = newRep
        self.size[newRep] = size1+size2
        if not self.isViolated():
            # print('tru',self.representatives,oldRep,newRep)
            return True
        
        self.representatives[oldRep] = oldRep
        self.size[newRep] = max(size1,size2)
        return False
           
    def isConnected(self,x,y):
        return self.find(x)==self.find(y)

    def isViolated(self):
        for rest in self.restrictions:
            if self.isConnected(rest[0],rest[1]):
                # print(rest)
                # print(self.representatives)
                return True

        return False