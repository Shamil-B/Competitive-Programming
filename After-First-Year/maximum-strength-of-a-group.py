class Solution:
    def maxStrength(self, nums: List[int]) -> int:
        max_ = 1
        negatives = []
        positives = []

        for num in nums:
            if num < 0:
                negatives.append(num)
            elif num > 0:
                positives.append(num)

        if not positives and len(negatives) <= 1:
            return max(nums)

        negatives.sort()
        if len(negatives)%2:
            for i in range(len(negatives)-1):
                max_ *= negatives[i]
        else:
            for i in range(len(negatives)):
                max_ *= negatives[i]

        for num in positives:
            max_ *= num

        return max(max_, max(nums))

        