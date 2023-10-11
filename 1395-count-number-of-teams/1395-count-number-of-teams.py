class Solution:
    def numTeams(self, rating: List[int]) -> int:
        size = len(rating)

        @cache
        def solveInc(ind, team_members):
            if ind >= size:
                return 0
            
            if team_members == 3:
                return 1

            ways = 0
            for i in range(ind+1, size):
                if rating[i] > rating[ind]:
                    ways += solveInc(i, team_members+1)

            return ways
        
        @cache
        def solveDec(ind, team_members):
            if ind >= size:
                return 0
            
            if team_members == 3:
                return 1

            ways = 0
            for i in range(ind+1, size):
                if rating[i] < rating[ind]:
                    ways += solveDec(i, team_members+1)

            return ways
        
        teamInc = teamDec = 0
        
        for i in range(size):
            teamInc += solveInc(i, 1)

        for i in range(size):
            teamDec += solveDec(i, 1)

        return teamInc + teamDec