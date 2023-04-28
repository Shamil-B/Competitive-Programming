class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        
        def areSimilar(s1,s2):
            size = len(s1)
            diff = 0

            for i in range(size):
                if s1[i]!=s2[i]:
                    diff += 1
                    
                if diff>2:
                    return False
                
            return True
        
        def explore(s):
            
            q = deque([s])
            visited = set()
            used = set()
            
            while q:
                curStr = q.popleft()
                
                if curStr in visited:
                    continue
                    
                visited.add(curStr)
                self.explored.add(curStr)
        
                for neigStr in strs:
                    if areSimilar(curStr,neigStr) and neigStr!=curStr:
                        q.append(neigStr)
                        
        self.explored = set()
        numberOfGroups = 0

        for s in strs:
            if s not in self.explored:
                explore(s)
                numberOfGroups += 1

        return numberOfGroups