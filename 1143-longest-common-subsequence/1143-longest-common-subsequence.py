class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        @cache
        def solve(ind1, ind2):
            if ind1 >= len(text1) or ind2 >= len(text2):
                return 0
            
            # if same move both
            if text1[ind1] == text2[ind2]:
                return solve(ind1+1, ind2+1) + 1

            # if different we have two options
            # move first
            first = solve(ind1+1, ind2)

            # move second
            second = solve(ind1, ind2+1)
            
            return max(first, second)
        
        return solve(0, 0)