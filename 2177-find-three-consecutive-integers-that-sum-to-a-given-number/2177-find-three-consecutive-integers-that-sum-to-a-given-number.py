class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        res = num//3
        if 3*res == num:
            return [res-1,res,res+1]
        
        return []