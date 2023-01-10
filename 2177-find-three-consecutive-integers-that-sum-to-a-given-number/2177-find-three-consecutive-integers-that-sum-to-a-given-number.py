class Solution:
    def sumOfThree(self, num: int) -> List[int]:

        if 3*(num//3) == num:
            return [num//3-1,num//3,num//3+1]
        
        return []