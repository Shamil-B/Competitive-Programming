class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        @cache
        def solve(ind,word):
            if ind >= len(s):
                if not word or word in dictionary:
                    return 0
                return len(word)
            
            if word and word not in dictionary:
                return solve(ind+1,word+s[ind])
            
            # three options
            # continue building up the word
            cont = solve(ind+1,word+s[ind])
            # break and include current letter in next word
            inc = solve(ind+1,s[ind])
            # break and exclude current letter in next word
            exc = solve(ind+1,"") + 1
            
            return min(cont,inc,exc)
        
        return solve(0,"")