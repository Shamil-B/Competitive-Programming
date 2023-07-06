class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstNumber = secondNumber = float('inf') 

        for num in nums: 
            if num <= firstNumber: 
                firstNumber = num

            elif num <= secondNumber:
                secondNumber = num

            else:
                return True

        return False