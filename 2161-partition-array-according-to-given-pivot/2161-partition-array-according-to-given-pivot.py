class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        middle = 0
        right = []
        
        for num in nums:
            if num < pivot:
                left += [num]
                
            elif num == pivot:
                middle += 1
                
            else:
                right += [num]
                
                
        return left + [pivot for i in range(middle)] + right