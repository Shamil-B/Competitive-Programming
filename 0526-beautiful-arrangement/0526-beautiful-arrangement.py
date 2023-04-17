class Solution:
    def countArrangement(self, n: int) -> int:
        explored = [False] * (n+1)
        res = 0
        def backtrack(ind):
            nonlocal res 
            if ind  == n+1:
                res +=1
            
            for index in range(1,n+1):
                if not explored[index]:
                    if index % ind == 0 or ind % index == 0:
                        explored[index] = True
                        backtrack(ind+1)
                        explored[index] = False
                        
        backtrack(1)
        return res