class Solution:
    def peakIndexInMountainArray(self, arr) -> int:
        n = len(arr)
        low = -1
        high = n
        
        while low+1<high:
            mid = low + (high - low)//2
            
            if (mid<n-1 and arr[mid] < arr[mid+1]) or (mid>0 and arr[mid]>arr[mid-1]):
                low = mid
                
            else:
                high = mid
                
                
        return low