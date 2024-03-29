class Solution(object):
    def PredictTheWinner(self, nums):
        
        dic = {}

        def find(i, j):
            if (i, j) not in dic:
                if i == j:
                    return nums[i]
                dic[i,j] = max(nums[i]-find(i+1, j), nums[j]-find(i, j-1))
            return dic[i,j]

        return find(0, len(nums)-1) >= 0