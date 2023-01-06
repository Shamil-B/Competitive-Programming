class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        positives = []
        negatives = []
        combinedArray = []
        
        for num in nums:
            if num > 0:
                positives.append(num)
                
            else:
                negatives.append(num)
                
        for i in range(len(nums)//2):
            combinedArray.append(positives[i])
            combinedArray.append(negatives[i])
            
        return combinedArray