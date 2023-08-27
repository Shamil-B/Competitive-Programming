class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        
        size = len(arr)
        @cache
        def solve(ind):
            if ind >= size or ind < 0 or ind in visited:
                return False
            
            if arr[ind] == 0:
                return True
            
            visited.add(ind)
            
            forward = solve(ind+arr[ind])
            backward = solve(ind-arr[ind])
            
            return forward or backward
        
        visited = set()
        return solve(start)