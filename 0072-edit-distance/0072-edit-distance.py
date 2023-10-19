class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        @cache
        def solve(ind1, ind2):
            if ind1 >= len(word1):
                return abs(len(word2) - ind2)
            
            if ind2 >= len(word2):
                return abs(len(word1) - ind1)

            # if the same either remove or continue
            if word1[ind1] == word2[ind2]:
                return min(solve(ind1+1, ind2)+1, solve(ind1+1, ind2+1))

            # else either remove or change or insert
            else:
                return min(solve(ind1+1, ind2)+1, solve(ind1+1, ind2+1)+1, solve(ind1, ind2+1)+1)
            
        return solve(0, 0)