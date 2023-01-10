class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res = num//3
        if num%3 == 0:
            return [res-1,res,res+1]
        
        return []
        
        