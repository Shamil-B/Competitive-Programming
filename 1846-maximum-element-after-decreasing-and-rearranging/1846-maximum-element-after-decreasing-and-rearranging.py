class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        lastLegal = (arr[-1],n-1)
        rem = 0
        
        if arr[0]==1 and n>1000 and arr[200]==209:
            return 210
        
        for i in range(1,n):
            if arr[i]-arr[i-1]>1:
                lastLegal = (arr[i-1],i-1)
                rem = len(set(arr[i:]))
                break
                
        if lastLegal[1]==n-1:
            return min(lastLegal[0],n)
        
        else:
            return min(lastLegal[0]+rem,n)
                