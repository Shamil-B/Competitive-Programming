from sortedcontainers import SortedList

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        cost = 0
        sortedList = SortedList()

        for num in instructions:
            cost += min(sortedList.bisect_left(num), len(sortedList) - sortedList.bisect_right(num))
            sortedList.add(num)

        return cost % (10**9 + 7)
        
    def calculateCost(self,nums,num):
        leftCost = bisect_left(nums,num)
        rightCost = len(nums) - bisect_right(nums,num)

        return min(leftCost,rightCost)     
            