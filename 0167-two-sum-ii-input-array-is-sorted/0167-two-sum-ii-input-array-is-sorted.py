class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        ptr1 = 0
        ptr2 = n-1
        
        while ptr1 < ptr2:
            summ = numbers[ptr1] + numbers[ptr2]
            if summ == target:
                return [ptr1+1,ptr2+1]
            
            elif summ < target:
                ptr1 += 1

            else:
                ptr2 -= 1