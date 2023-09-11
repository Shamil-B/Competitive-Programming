class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        ans = []
        wordDict = set(wordDict)

        @cache
        def solve(ind,sent,word):
            if ind >= len(s):
                if word in wordDict:
                    sent += " " + word
                    ans.append(sent)
                return
                    
            if word in wordDict:
                solve(ind+1,sent+" "+word,s[ind])
            solve(ind+1,sent,word+s[ind])

        solve(0,"","")
        for i in range(len(ans)):
            ans[i] = ans[i][1:]

        return ans