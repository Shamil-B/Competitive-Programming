class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(target)
        self.representatives = {i:i for i in range(n)}
        self.size = [1 for i in range(n)]

        for swap in allowedSwaps:
            self.union(swap[0],swap[1])

        groups = defaultdict(list)
        for i in range(len(self.representatives)):
            groups[self.find(i)].append(i)

        diff = 0
        for grp in groups.values():
            sett = defaultdict(int)
            for i in grp:
                sett[source[i]]+=1

            for i in grp:
                if target[i] not in sett or sett[target[i]]<1:
                    diff += 1
                    
                else:
                    sett[target[i]] -= 1
                    
        return diff

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

        size1 = self.size[newRep-1]
        size2 = self.size[oldRep-1]

        if size1 < size2:
            newRep,oldRep = oldRep,newRep

        self.representatives[oldRep] = newRep
        self.size[newRep-1] = size1+size2
