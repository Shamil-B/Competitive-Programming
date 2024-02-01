class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        ans = [[]]
        nums.sort()
        for i in range(len(nums)):
            if len(ans[-1]) == 3:
                ans.append([])
            
            if ans[-1] and abs(ans[-1][0] - nums[i]) > k:
                return []

            ans[-1].append(nums[i])
                
        return ans