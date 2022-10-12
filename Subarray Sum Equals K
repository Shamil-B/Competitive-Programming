class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans, size = 0, len(nums)
        pfs = [nums[0]]
        dic = {}
        dic[0] = 1
        for i in nums[1:]:
            pfs.append(i+pfs[-1])
        for i in pfs:
            if i-k in dic:
                ans+=dic[i-k]
            dic[i] = dic.get(i,0) + 1 
        return ans
