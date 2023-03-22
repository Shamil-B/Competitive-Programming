class Solution:
    def sortArray(self, nums):
        
        def mergeSort(left,right):
            if left == right:
                return [nums[left]]
            
            mid = (left+right)//2
            
            leftArr = mergeSort(left,mid)
            rightArr = mergeSort(mid+1,right)
            
            return self.merge(leftArr,rightArr)
        
        return mergeSort(0,len(nums)-1)
        
        
    def merge(self,arr1,arr2):
        
        p1 = p2 = 0
        mergedArr = []
        n = len(arr1)
        m = len(arr2)
        while p1<n or p2<m:
            
            if p2 == m or (p1<n and arr1[p1] <= arr2[p2]):
                mergedArr.append(arr1[p1])
                p1 += 1
                
            elif p1 == n or (p2<m and arr1[p1] > arr2[p2]):
                mergedArr.append(arr2[p2])
                p2 += 1
                
                
        return mergedArr