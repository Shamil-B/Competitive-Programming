class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        size = len(t)
        @cache
        def solve(ind,word):
            if word == s:
                return True

            if len(word) > len(s) or ind >= size or word != s[:len(word)] :
                return False

            return solve(ind+1,word) or solve(ind+1,word+t[ind])
        
        return solve(0,"")