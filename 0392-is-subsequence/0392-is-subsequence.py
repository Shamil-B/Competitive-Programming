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
        
        # return solve(0,"")

        p1 = p2 = 0
        for i in range(size):
            if p1 >= len(s):
                break

            if s[p1] == t[p2]:
                p1 += 1
                p2 += 1
                
            else:
                p2 += 1
                
        if p1 == len(s):
            return True
        
        return False