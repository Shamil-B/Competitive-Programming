class Solution:
    def combine(self, n, k) -> List[List[int]]:
        self.finalArr = []
        
        def backTrack(arr,s):

            if len(arr) == k:
                self.finalArr.append(arr[:])
                return

            candidates = [i for i in range(s+1,n+1)]
            for candidate in candidates:
                arr.append(candidate)
                
                backTrack(arr[:],candidate)      
                
                arr.pop()
                
        backTrack([],0)
        
        return self.finalArr
    
    