class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def solve(ind,word):
            if ind >= len(s):
                if not word or word in wordDict:
                    return True
                return False

            if word in wordDict:
                return solve(ind+1,s[ind]) or solve(ind+1,word+s[ind])

            return solve(ind+1,word+s[ind])
        
        return solve(0,"")
            
                