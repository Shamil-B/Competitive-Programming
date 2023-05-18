class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        self.representatives = {}
        self.heights = {}
        
        for account in accounts:
            for i in range(1,len(account)):
                self.representatives[account[i]] = account[i]
                self.heights[account[i]] = 1
                
        for account in accounts:
            for i in range(1,len(account)-1):
                self.union(account[i],account[i+1])
     
        for index1 in range(len(accounts)):
            for index2 in range(len(accounts)):
                if accounts[index1] and accounts[index2] and accounts[index1][0] == accounts[index2][0] and index1!=index2:
                    if self.find(accounts[index1][1]) == self.find(accounts[index2][1]):
                        accounts[index1] += accounts[index2][1:]
                        accounts[index2] = []
        answer = []
        
        for i in range(len(accounts)):
            if accounts[i]:
                label = accounts[i][0]
                accounts[i] = [label]+sorted(list(set(accounts[i][1:])))

        for account in accounts:
            if account:
                answer.append([account[0]]+(account[1:]))
                
        return answer

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
