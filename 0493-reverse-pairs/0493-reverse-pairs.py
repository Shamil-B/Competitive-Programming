class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        self.pairs = 0
        def tweakedMergeSort(nums):
            
            if len(nums)==1:
                return nums
            
            mid = len(nums)//2
            left = tweakedMergeSort(nums[:mid])
            right = tweakedMergeSort(nums[mid:])
            
            
            for i in range(len(right)):
                target = right[i]*2
                targetIndex = bisect_right(left,target)
                self.pairs += (len(left)-targetIndex)
                
            
            return self.merge(left,right)

        tweakedMergeSort(nums)
        return self.pairs
        
    def merge(self,arr1,arr2):
            merged = []
            n = len(arr1)
            m = len(arr2)
            p1 = p2 = 0
            
            while p1<n or p2<m:
                
                if p2==m or (p1<n and arr1[p1]<arr2[p2]):
                    merged.append(arr1[p1])
                    p1 += 1
                
                elif p1==n or (p2<m and arr1[p1]>=arr2[p2]):
                    merged.append(arr2[p2])
                    p2+=1
                    
            return merged
        
    