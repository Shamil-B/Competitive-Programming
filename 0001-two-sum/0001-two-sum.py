class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        p1 = 0
        p2 = n-1
        dic = {}


        for ind in range(n):
            if nums[ind] in dic:
                dic[nums[ind]].append(ind)
            else:
                dic[nums[ind]] = [ind]

        nums.sort()

        while p1<p2:
            if nums[p1]+nums[p2]<target:
                p1+=1
            elif nums[p1]+nums[p2]>target:
                p2-=1

            else:
                return [dic[nums[p1]].pop(0),dic[nums[p2]].pop(0)]
                