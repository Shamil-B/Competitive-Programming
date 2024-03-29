class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        result = []
        sortedList = self.sortList(nums)
        for index in range(len(sortedList)):
            if sortedList[index]==target:
                result.append(index)
                
        
        return result
                
                
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