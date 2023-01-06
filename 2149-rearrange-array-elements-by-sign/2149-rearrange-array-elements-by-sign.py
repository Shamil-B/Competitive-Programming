class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positives = []
        negatives = []
        combinedArray = []
        
        for num in nums:
            if num > 0:
                combinedArray.append(num)
                combinedArray.append(0)
                
        oddIndex = 1
        for num in nums:
            
            if num < 0 and oddIndex < len(combinedArray):
                combinedArray[oddIndex] = num
                oddIndex += 2
        
        
       
        return combinedArray