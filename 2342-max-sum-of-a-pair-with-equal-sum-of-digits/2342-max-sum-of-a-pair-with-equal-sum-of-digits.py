class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        mapping = {}
        #construct the mapping

        for num in nums:
            key = sum(list(map(int,list(str(num)))))
            if key in mapping:
                mapping[key].append(num)

            else:
                mapping[key] = [num]

        max_ = -1
        for key in mapping.keys():
            if len(mapping[key])>1:
                firstMax = max(mapping[key])
                mapping[key].remove(firstMax)
                secondMax = max(mapping[key])
                max_ = max(max_,firstMax+secondMax)

        return max_