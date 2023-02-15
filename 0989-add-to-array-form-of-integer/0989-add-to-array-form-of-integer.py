class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        
        nums = list(map(str,num))
        nums = ''.join(nums)
        res = str(int(nums) + k)
        
        arr = []
        for num in res:
            arr.append(int(num))
            
        return arr