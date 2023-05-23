class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # we do the union find

        self.representatives = [i for i in range(len(s))]
        self.size = [1 for i in range(len(s))]
        self.chars = defaultdict(list)

        # now for every edge we are going to construct the union graph
        for idx1,idx2 in pairs:
            self.union(idx1,idx2)
            
        for index,item in enumerate(self.representatives):
            self.representatives[index] = self.find(item)
            
        for index,item in enumerate(self.representatives):
            self.chars[item].append(s[index])
            
        for key in self.chars.keys():
            self.chars[key] = sorted(self.chars[key],reverse=True)
        
        ans = ""
        for item in self.representatives:
            ans += self.chars[item].pop()
        
        
        return ans

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
        size1 = self.size[x-1]
        size2 = self.size[y-1]

        if size1 > size2:
            newRep = self.find(x)
            oldRep = self.find(y)

        else:
            newRep = self.find(y)
            oldRep = self.find(x)

        self.representatives[oldRep] = newRep
        self.size[newRep] = size1+size2