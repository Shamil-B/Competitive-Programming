class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        #make it one array
        
        self.pairs = 0
        nums = []
        n = len(nums1)
        self.k = diff
        for i in range(n):
            nums.append(nums1[i]-nums2[i])
        
        def mergeSort(nums):

            if len(nums)==1:
                return nums
            
            mid = len(nums)//2
            left = mergeSort(nums[:mid])
            right = mergeSort(nums[mid:])
            
            for i in range(len(left)):
                target = left[i]-self.k
                #how many numbers from right are greater than target
                targetIndex = bisect_left(right,target)
                count = len(right)-targetIndex
                self.pairs += count

            return merge(left,right)
        
        def merge(arr1,arr2):
            p1 = p2 = 0
            
            n = len(arr1)
            m = len(arr2)
            res = []
            while p1<n or p2<m:
                if p2==m or (p1<n and arr1[p1]<=arr2[p2]):
                    res.append(arr1[p1])
                    p1 += 1
                    
                elif p1==n or (p2<m and arr2[p2]<arr1[p1]):
                    res.append(arr2[p2])
                    p2 += 1
                    
            return res
        
        mergeSort(nums)
        return self.pairs