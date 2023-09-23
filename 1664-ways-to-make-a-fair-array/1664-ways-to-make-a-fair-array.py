class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        forward = {}
        backward = {}
        n = len(nums)
        odd = even = 0
        for i in range(n):
            forward[i] = (odd,even)
            if i%2:
                odd += nums[i]
            else:
                even += nums[i]

        odd = even = 0
        for i in range(n-1,-1,-1):
            backward[i] = (even,odd)
            if i%2:
                odd += nums[i]
            else:
                even += nums[i]

        numOfFairArrays = 0
        for i in range(n):
            if (forward[i][0]+backward[i][0]) == (forward[i][1]+backward[i][1]):
                numOfFairArrays += 1

        return numOfFairArrays