class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxx = arr[-1]
        for i in range(len(arr)-2,-1,-1):
            tmp = arr[i]
            arr[i] = maxx
            
            if tmp>maxx:
                maxx = tmp
            
        arr[-1] = -1
        
        return arr