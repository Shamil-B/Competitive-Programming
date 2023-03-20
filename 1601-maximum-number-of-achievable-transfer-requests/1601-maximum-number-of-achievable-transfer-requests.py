class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
        self.max = 0
        self.state = [0]*n
        
        def backtrack(path,ind):
            if not any(self.state):
                self.max = max(self.max,len(path))
                
            for i in range(ind,len(requests)):
                
                path.append(requests[i])
                self.doOperation(requests[i],True)

                backtrack(path,i+1)

                self.doOperation(requests[i],False)
                path.pop()
                
        backtrack([],0)
        return self.max
    
    def doOperation(self,req,forward):
        
        if forward:
            self.state[req[0]] += 1
            self.state[req[1]] -= 1

        else:
            self.state[req[0]] -= 1
            self.state[req[1]] += 1
            
        
        
        
        
        