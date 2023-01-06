class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        size = len(nums)
        combinedArray = [0 for i in range(size)]
        
        oddIndex = 1
        evenIndex = 0
        for num in nums:
            if num > 0 and evenIndex < size:
                combinedArray[evenIndex] = num
                evenIndex += 2
                
            else:
                if oddIndex < size:
                    combinedArray[oddIndex] = num
                    oddIndex += 2
        
        return combinedArray