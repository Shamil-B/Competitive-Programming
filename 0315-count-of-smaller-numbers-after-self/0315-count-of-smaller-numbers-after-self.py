class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.counts = [0]*len(nums)
        modNums = []
        for i in range(len(nums)):
            modNums.append((nums[i],i))

        
        def tweakedMergeSort(nums):
                if len(nums)==1:
                    return nums
                
                mid = len(nums)//2
                left = tweakedMergeSort(nums[:mid])
                right = tweakedMergeSort(nums[mid:])

                newRight = self.purify(right)
                for i in range(len(left)):
                    target = left[i][0]
                    targetIndex = bisect_left(newRight,target)
                    self.counts[left[i][1]] += targetIndex

                return self.merge(left,right)
            
        tweakedMergeSort(modNums)
        return self.counts

    def merge(self,arr1,arr2):
        p1 = p2 = 0
        
        n = len(arr1)
        m = len(arr2)
        merged = []
        
        while p1<n or p2<m:
            
            if p2>=m or (p1<n and arr1[p1][0]<=arr2[p2][0]):
                merged.append(arr1[p1])
                p1 += 1
                
            elif p1>=n or (p2<m and arr1[p1][0]>arr2[p2][0]):
                merged.append(arr2[p2])
                p2 += 1

        return merged
    
    def purify(self,arr):
        newArr = []
        
        for num in arr:
            newArr.append(num[0])
            
        return newArr
    
    