class Solution:
    def splitString(self, st: str) -> bool:
        
        self.found = False
        def backTrack(arr,s):

            if s=="":
                if self.validate(arr):
                    self.found = True

            candidates = [s[:i] for i in range(1,len(s)+1)]

            for ind,candidate in enumerate(candidates):
                if not arr or arr[-1] - int(candidate) == 1:
                    arr.append(int(candidate))
                    backTrack(arr,s[ind+1:])
                    arr.pop()
           
        backTrack([],st)
        return self.found

    def validate(self,arr):
        if len(arr)==1:
            return False
        
        for i in range(1,len(arr)):
            if arr[i]-arr[i-1] != -1:
                return False
            
        return True