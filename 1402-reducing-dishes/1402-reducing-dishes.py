class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        n = len(satisfaction)
        satisfaction.sort()

        positiveStart = 0
        for i in range(n):
            if satisfaction[i] > 0:
                positiveStart = i
                break

        reserveSum = sum(satisfaction[positiveStart:])
        negSum = sum(satisfaction[:positiveStart])
        finalSum = 0

        j = 1
        for i in range(n):
            if satisfaction[i] < 0:
                negSum -= satisfaction[i]
                value = satisfaction[i]*(j) + negSum
                
            else:
                value = satisfaction[i]*(j)

            if value + reserveSum > 0:
                print(i)
                finalSum += satisfaction[i]*(j)
                j += 1
                
        return finalSum