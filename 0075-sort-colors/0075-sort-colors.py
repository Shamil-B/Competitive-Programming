class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums2 = self.sortList(nums)
        for i in range(len(nums)):
            nums[i] = nums2[i]
                
    def sortList(self,arr):
        if len(arr)==1:
            return arr
        
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        
        return self.merge(self.sortList(left),self.sortList(right))
    
    
    
    def merge(self,l1,l2):
        ind1 = 0
        ind2 = 0
        res = []
        while ind1<len(l1) and ind2<len(l2):
            if l1[ind1]<l2[ind2]:
                res.append(l1[ind1])
                ind1+=1
                
            else:
                res.append(l2[ind2])
                ind2+=1
                
        while ind1<len(l1):
            res.append(l1[ind1])
            ind1+=1
            
        while ind2<len(l2):
            res.append(l2[ind2])
            ind2+=1
            
        return res