class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num%3 != 0:
            return []
        
        res = num//3
        return [res-1,res,res+1]