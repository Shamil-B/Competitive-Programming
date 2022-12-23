class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        dic = {}

        for i in range(n):
            if nums[i] not in dic:
                dic[nums[i]] = 0
            else:
                dic[nums[i]] += 1

        dicKeys = list(dic.keys()) # to iterate through the dictionary           
        for i in dicKeys:
            summ = 0
            for k in range(dic[i],-1,-1):
                summ += k

            count+=summ

        return count