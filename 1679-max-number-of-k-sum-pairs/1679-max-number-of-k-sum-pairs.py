class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pt1 = 0
        pt2 = n-1
        op = 0
        
        nums.sort()
        
        while pt1<pt2:
            summ = nums[pt1] + nums[pt2]
            if summ == k:
                op += 1
                pt1 += 1
                pt2 -= 1
                
            elif summ < k:
                pt1 += 1
                
            else:
                pt2 -= 1
                
        return op