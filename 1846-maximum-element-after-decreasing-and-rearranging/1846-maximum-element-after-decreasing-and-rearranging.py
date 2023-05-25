class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        n = len(arr)
        max_ = 1
        
        arr[0] = 1
        for i in range(1,n):
            if arr[i]-arr[i-1]>1:
                arr[i] = arr[i-1]+1
                
            max_ = max(arr[i],max_)
            
        return max_
                
 