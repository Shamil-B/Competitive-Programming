class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        @cache
        def solve(ind,word):
            if word == t:
                return 1

            if len(word) > len(t) or ind >= len(s) or word != t[:len(word)]:
                return 0

            return solve(ind+1,word) + solve(ind+1,word+s[ind])

        return solve(0,"") % (10**9+7)