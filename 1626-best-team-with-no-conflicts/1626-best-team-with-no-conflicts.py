class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        size = len(scores)
        teams = []
        for i in range(size):
            teams.append((ages[i], scores[i]))

        teams.sort()
        
        def isValidAction(ind1,ind2):
            if teams[ind1][0] < teams[ind2][0] and teams[ind1][1] > teams[ind2][1]:
                return False

            return True

        @cache
        def solve(ind):
            max_ = teams[ind][1]
            for i in range(ind+1, size):
                if isValidAction(ind,i):
                    max_ = max(max_, solve(i) + teams[ind][1])

            return max_

#         max_ = 0
#         for i in range(size):
#             max_ = max(max_, solve(i))

#         return max_

        def solveBottomUp():
            dp = [teams[i][1] for i in range(size)]
            for i in range(size):
                for j in range(i+1,size):
                    if isValidAction(i,j):
                        dp[j] = max(dp[j],dp[i]+teams[j][1])
            print(dp)
            return max(dp)
    
        return solveBottomUp()