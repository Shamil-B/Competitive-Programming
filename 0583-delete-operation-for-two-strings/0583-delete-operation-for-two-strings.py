class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def solve(ind_1, ind_2):
            if ind_1 >= len(word1):
                return len(word2) - ind_2
            
            if ind_2 >= len(word2):
                return len(word1) - ind_1
            
            if word1[ind_1] == word2[ind_2]:
                return solve(ind_1 + 1, ind_2 + 1)
            
            return min(solve(ind_1 + 1, ind_2), solve(ind_1, ind_2 + 1)) + 1
        
        return solve(0, 0)